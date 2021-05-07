"""
Entry point for training and evaluating a Bi-LSTM language identifier
"""

import argparse
import json
import os
import random
import torch

from datetime import datetime
from stanza.models.langid.data import DataLoader
from stanza.models.langid.trainer import Trainer
from tqdm import tqdm


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", help="batch size for training", type=int, default=64)
    parser.add_argument("--data-dir", help="directory with train/dev/test data", default=None)
    parser.add_argument("--load-model", help="path to load model from", default=None)
    parser.add_argument("--mode", help="train or eval", default="train")
    parser.add_argument("--num-epochs", help="number of epochs for training", type=int, default=50)
    parser.add_argument("--randomize", help="take random substrings of samples", action="store_true")
    parser.add_argument("--randomize-range", help="range of lengths to use when random sampling text", 
                        type=randomize_range, default="5,20")
    parser.add_argument("--save-name", help="where to save model", default=None)
    parser.add_argument("--use-gpu", help="whether to use gpu", type=bool, default=True)
    args = parser.parse_args(args=args)
    return args


def randomize_range(range_list):
    return [int(x) for x in range_list]


def main(args=None):
    args = parse_args(args=args)
    if args.mode == "train":
        train_model(args)
    else:
        eval_model(args)


def build_indexes(args):
    tag_to_idx = {}
    char_to_idx = {}
    train_files = [f"{args.data_dir}/{x}" for x in os.listdir(args.data_dir) if "train" in x]
    for train_file in train_files:
        lines = open(train_file).read().split("\n")
        examples = [json.loads(line) for line in lines if line.strip()]
        for example in examples:
            label = example["label"]
            if label not in tag_to_idx:
                tag_to_idx[label] = len(tag_to_idx)
            sequence = example["text"]
            for char in list(sequence):
                if char not in char_to_idx:
                    char_to_idx[char] = len(char_to_idx)
    char_to_idx["UNK"] = len(char_to_idx)
    char_to_idx["<PAD>"] = len(char_to_idx)

    return tag_to_idx, char_to_idx


def train_model(args):
    # set up indexes
    tag_to_idx, char_to_idx = build_indexes(args)
    # load training data
    train_data = DataLoader()
    train_files = [f"{args.data_dir}/{x}" for x in os.listdir(args.data_dir) if "train" in x]
    train_data.load_data(args.batch_size, train_files, char_to_idx, tag_to_idx, args.randomize)
    # load dev data
    dev_data = DataLoader()
    dev_files = [f"{args.data_dir}/{x}" for x in os.listdir(args.data_dir) if "dev" in x]
    dev_data.load_data(args.batch_size, dev_files, char_to_idx, tag_to_idx, randomize=False)
    # set up trainer
    trainer_config = {
        "model_path": args.save_name,
        "char_to_idx": char_to_idx,
        "tag_to_idx": tag_to_idx,
        "batch_size": args.batch_size,
        "lang_weights": train_data.lang_weights
    }
    if args.load_model:
        trainer_config["load_model"] = args.load_model
        print(f"{datetime.now()}\tLoading model from: {args.load_model}")
    trainer = Trainer(trainer_config, args.use_gpu)
    # run training
    best_accuracy = 0.0
    for epoch in range(1, args.num_epochs+1):
        print(f"{datetime.now()}\tEpoch {epoch}")
        print(f"{datetime.now()}\tNum training batches: {len(train_data.batches)}")
        for train_batch in tqdm(train_data.batches):
            inputs = (train_batch["sentences"], train_batch["targets"])
            trainer.update(inputs)
        print(f"{datetime.now()}\tEpoch complete. Evaluating on dev data.")
        curr_dev_accuracy, curr_confusion_matrix, curr_precisions, curr_recalls, curr_f1s = \
            eval_trainer(trainer, dev_data)
        print(f"{datetime.now()}\tCurrent dev accuracy: {curr_dev_accuracy}")
        if curr_dev_accuracy > best_accuracy:
            print(f"{datetime.now()}\tNew best score. Saving model.")
            trainer.save()
            with open(score_log_path(args.save_name), "w") as score_log_file:
                for score_log in [{"dev_accuracy": curr_dev_accuracy}, curr_confusion_matrix, curr_precisions,
                                  curr_recalls, curr_f1s]:
                    score_log_file.write(json.dumps(score_log) + "\n")
            best_accuracy = curr_dev_accuracy

        # reload training data
        print(f"{datetime.now()}\tResampling training data.")
        train_data.load_data(args.batch_size, train_files, char_to_idx, tag_to_idx, args.randomize)


def score_log_path(file_path):
    """
    Helper that will determine corresponding log file (e.g. /path/to/demo.pt to /path/to/demo.json
    """
    model_suffix = file_path.split(".")[-1]
    return f"{file_path[:-1 * len(model_suffix)]}json"


def eval_model(args):
    # set up trainer
    trainer_config = {
        "model_path": None,
        "load_model": args.load_model,
        "batch_size": args.batch_size
    }
    trainer = Trainer(trainer_config, load_model=True, use_gpu=args.use_gpu)
    # load test data
    test_data = DataLoader()
    test_files = [f"{args.data_dir}/{x}" for x in os.listdir(args.data_dir) if "test" in x]
    test_data.load_data(args.batch_size, test_files, trainer.model.char_to_idx, trainer.model.tag_to_idx, 
                        randomize=False)
    curr_dev_accuracy, curr_confusion_matrix, curr_precisions, curr_recalls, curr_f1s = \
        eval_trainer(trainer, test_data)
    print(f"{datetime.now()}\tDev accuracy: {curr_dev_accuracy}")
    if not os.path.exists(score_log_path(args.load_model)):
        with open(score_log_path(args.load_model), "w") as score_log_file:
            for score_log in [{"dev_accuracy": curr_dev_accuracy}, curr_confusion_matrix, curr_precisions,
                              curr_recalls, curr_f1s]:
                score_log_file.write(json.dumps(score_log) + "\n")
        


def eval_trainer(trainer, dev_data):
    """
    Produce dev accuracy and confusion matrix for a trainer
    """

    # set up confusion matrix
    tag_to_idx = trainer.model.tag_to_idx
    idx_to_tag = trainer.model.idx_to_tag
    confusion_matrix = {}
    for row_label in tag_to_idx:
        confusion_matrix[row_label] = {}
        for col_label in tag_to_idx:
            confusion_matrix[row_label][col_label] = 0

    # process dev batches
    for dev_batch in tqdm(dev_data.batches):
        inputs = (dev_batch["sentences"], dev_batch["targets"])
        predictions = trainer.predict(inputs)
        for target_idx, prediction in zip(dev_batch["targets"], predictions):
            confusion_matrix[idx_to_tag[target_idx]][idx_to_tag[prediction]] += 1

    # calculate dev accuracy
    total_examples = sum([sum([confusion_matrix[i][j] for j in confusion_matrix[i]]) for i in confusion_matrix])
    total_correct = sum([confusion_matrix[i][i] for i in confusion_matrix])
    dev_accuracy = float(total_correct) / float(total_examples)

    # calculate precision, recall, F1
    precision_scores = {"type": "precision"}
    recall_scores = {"type": "recall"}
    f1_scores = {"type": "f1"}
    for prediction_label in tag_to_idx:
        total = sum([confusion_matrix[k][prediction_label] for k in tag_to_idx])
        precision_scores[prediction_label] = float(confusion_matrix[prediction_label][prediction_label])/float(total)
    for target_label in tag_to_idx:
        total = sum([confusion_matrix[target_label][k] for k in tag_to_idx])
        recall_scores[target_label] = float(confusion_matrix[target_label][target_label])/float(total)
    for label in tag_to_idx:
        f1_scores[label] = \
            2.0 * (precision_scores[label] * recall_scores[label]) / (precision_scores[label] + recall_scores[label])

    return dev_accuracy, confusion_matrix, precision_scores, recall_scores, f1_scores


if __name__ == "__main__":
    main()
