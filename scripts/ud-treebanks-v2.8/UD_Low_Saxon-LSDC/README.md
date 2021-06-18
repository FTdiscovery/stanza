# Summary

The UD Low Saxon LSDC dataset consists of sentences in 18 Low Saxon dialects from both Germany and the Netherlands. These sentences are (or are to become) part of the LSDC dataset and represent the language from the 19th and early 20th century in genres such as short stories, novels, speeches, letters and fairytales. 


# Introduction

The UD Low Saxon LSDC dataset contains 18 Low Saxon dialects from both Germany and the Netherlands represented by 2 sentences each and belonging to the domains of short stories, novels, speeches, letters and fairytales. Each sentence was chosen from a different text to present some of the variation within the different dialect groups. Since there is no official interregional spelling, the interregional spelling suggestion used by e.g. the Dutch Low Saxon Wikipedia (_Nysassiske Skryvwyse_, described in more detail here: https://skryvwyse.eu/ (only in Low Saxon)) is used as a compromise for normalisation, but the original spelling of the source is included in the line "text_orig =" and a Middle Low Saxon lemma is added in the tenth column ("lemma[gml]=xxx") in order to make the Modern Low Saxon data more easily comparable with the Middle Low Saxon data in the reference corpus "Referenzkorpus Mittelniederdeutsch/Niederrheinisch". For this reason, the Middle Low Saxon lemma forms follow the "Mittelniederdeutsches Handwörterbuch" by Agathe Lasch et al. like in the reference corpus. Middle Low Saxon lemmata are only added in the cases where I have found an attestation in Middle Low Saxon, i.e. the word is either listed in the Handwörterbuch or is found in the reference corpus. I still include Middle Low Saxon lemmata if the word's meaning has changed, but I did not e.g. create new complex word lemmata from known simplex words and neither did I reconstruct potential Middle Low Saxon forms for words which have not yet been attested at that stage of the language.

The dataset contains only sentences from copyright-free material from the 19th and early 20th century. Part of the sentences are already included in the first release of the LSDC dataset found here: https://github.com/Helsinki-NLP/LSDC/ See there for further information on the origin of the data. The other sentences originate mostly from Joh. A. Leopold's work 'Van de Schelde tot te Weichsel', a digitised version of which is accessible here: https://www.dbnl.org/titels/titel.php?id=leop008sche00 An exception constitutes the first sentence which is taken from a text to be found in the Twentse Taalbank: http://www.twentsetaalbank.nl/docs/TWA.1894-Heinink-Krisjaon_Klaover-150.pdf These other sentences will be added to the next release of the LSDC dataset. 

Due to the small size of the first version of the dataset, it has not yet been split into training, development and test sets. The morphological features and relation subtypes are still missing but will be included in the next release. 


# Acknowledgments

The following people were involved in the creation of this dataset:

* Janine Siewert (data collection, selection and annotation)
* Jack Michael Rueter (annotation-related advice) 

## References

If you use this treebank, please cite this paper describing the LSDC dataset:

```
@inproceedings{siewert-etal-2020-lsdc,
	abstract = "We present a new comprehensive dataset for the unstandardised West-Germanic language Low Saxon covering the last two centuries, the majority of modern dialects and various genres, which will be made openly available in connection with the final version of this paper. Since so far no such comprehensive dataset of contemporary Low Saxon exists, this provides a great contribution to NLP research on this language. We also test the use of this dataset for dialect classification by training a few baseline models comparing statistical and neural approaches. The performance of these models shows that in spite of an imbalance in the amount of data per dialect, enough features can be learned for a relatively high classification accuracy.",
	address = "Barcelona, Spain (Online)",
	author = "Siewert, Janine and Scherrer, Yves and Wieling, Martijn and Tiedemann, Jörg",
	booktitle = "Proceedings of the 7th Workshop on NLP for Similar Languages, Varieties and Dialects",
	month = dec,
	pages = "25–35",
	publisher = "International Committee on Computational Linguistics (ICCL)",
	title = "{LSDC} - A comprehensive dataset for Low {S}axon Dialect Classification",
	url = "https://www.aclweb.org/anthology/2020.vardial-1.3",
	year = "2020"
}

```
### References used for the creation of this dataset: 

* Lasch, Agathe et al. 1928 ff. *Mittelniederdeutsches Handwörterbuch.* Neumünster: Wachholtz.
* ReN-Team. 2019. *Referenzkorpus Mittelniederdeutsch/Niederrheinisch (1200-1650).* Archived in Hamburger Zentrum für Sprachkorpora. Version 1.0. Publication date 2019-08-14. http://hdl.handle.net/11022/0000-0007-D829-8.


# Changelog

* 2021-05-15 v2.8
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.8
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction nonfiction
Lemmas: manual native
UPOS: manual native
XPOS: manual native
Features: manual native
Relations: manual native
Contributors: Siewert, Janine
Contributing: elsewhere
Contact: janine.siewert@helsinki.fi
===============================================================================
</pre>
