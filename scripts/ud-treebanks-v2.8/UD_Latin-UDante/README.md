# Summary

The **UDante** treebank is based on the Latin texts of Dante Alighieri, taken from the [**DanteSearch corpus**](https://dantesearch.dantenetwork.it), originally created at the University of Pisa, Italy. 

It is a treebank of Latin language, more precisely of **literary Medieval Latin** (XIVth century).

# Introduction

This treebank includes 1 721 sentences (55 697 tokens) and consists of
literary texts (letters, treatises, poetry). The treebank is licensed under the terms of
[CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/).

**UDante** includes the following Latin texts (mostly) by Dante Alighieri, or disputedly attibuted to him:

* *De vulgari eloquentia*:  13 493 tokens for 419 sentences over 2 books
* *Monarchia*: 22 764 tokens for 682 sentences over 3 books
* *Letters*: 11 667 tokens for 376 sentences over 13 letters
* *Questio de aqua et terra*: 5 111 tokens for 133 sentences
* *Eclogues*: 2 662 tokens for 111 sentences over 4 eclogues

The syntactic annotation of the **UDante** treebank has been created through a manual annotation process performed in the context of a collaboration between the University of Pisa (responsible: Mirko Tavoni) and the [**LiLa: Linking Latin project**](https://lila-erc.eu) at the Università Cattolica del Sacro Cuore, Milan, Italy (PI: Marco Passarotti). 
The annotation process was co-ordinated by Flavio Massimiliano Cecchini, Giovanni Moretti and Rachele Sprugnoli (all Università Cattolica del Sacro Cuore).

# Acknowledgments

The LiLa project has received funding from the European Research Council (ERC) under the European Union’s  _Horizon 2020 research and innovation programme – Grant Agreement No. 769994_.

We wish to thank all the annotators of the **UDante** treebank: Daniela Corbetta, Federica Favero, Federica Gamba, Martina de Laurentiis, Giulia Pedonese, Andrea Peverelli and Elena Vagnoni.

## References

* Flavio Massimiliano Cecchini, Rachele Sprugnoli, Giovanni Moretti, Marco Passarotti. 2020. *UDante: First Steps Towards the Universal Dependencies Treebank of Dante's Latin Works*. In: Johanna Monti, Felice Dell'Orletta, Fabio Tamburini (eds.), Proceedings of the Seventh Italian Conference on Computational Linguistics. CEUR Workshop Proceedings, pp. 1-7 ([link](http://ceur-ws.org/Vol-2769/paper_14.pdf)).


# Data and data split

## Corpus description

The **DanteSearch** corpus consists of all Latin works by Dante, Italian literate and politician of the XIVth century, originary of Florence, considered to be "the father of the Italian language" and most famous for its *Divina Commedia* (written in Tuscan literary Italian), and some related works. In particular:

* *De vulgari eloquentia* is a rhetoric and linguistic treaty about the best practices for the use of the "vulgar", i.e. vernacular language, as opposed to Latin;
* *Monarchia* is a political treaty about the relation between Empire and Church;
* the *Letters* are a collection of correspondence by Dante, mostly of political character. The collection includes letters in the name of other persons, and some incomplete letters. The actual authorship of the famous XIIIth letter to Cangrande della Scala (ruler of Verona) is disputed; 
* *Questio de aqua et terra* is a technical/philosophical dissertation about the shape of the Earth and the oceans, and is too of disputed authorship;
* the *Eclogues* are four poetic compositions of bucolic character in response to each other, two by Dante and two by Giovanni del Virgilio.


## Annotation

The following table schematically describes for each layer of the **UDante** treebank how it has been obtained with respect to the original **DanteSearch** corpus, which is annotated only for parts of speech and morphological features, following a proprietary tagset. 

| CoNLL-U Field | Source |
| ------ | ------ |
| ID | Sentence segmentation and tokenization is based on the original **DanteSearch** corpus, but has been manually, and partially automatically, modified in some cases (by means of both splits and merges of tokens or sentences) |
| FORM | Obtained from the **DanteSearch** corpus; some minor mistakes have been manually corrected |
| LEMMA | Obtained from the **DanteSearch** corpus, but manually and partially automatically modified (and in some cases corrected) in some occurrences in order to fit with changes in other annotation layers (part of speech, morpholexical features), or for reasons of standardization |
| UPOSTAG | Converted automatically from the **DanteSearch** tagset, but manually and partially automatically modified in order to fit with annotation solutions related to the UD formalism |
| XPOSTAG | As in the **DanteSearch** corpus (may be split or merged over multiple tokens if the tokenization has been changed) |
| FEATS |  Converted automatically from the **DanteSearch** tagset, but manually and partially automatically corrected, modified and augmented according to the UD formalism |
| HEAD | Manually annotated from scratch and later manually and partially automatically corrected |
| DEPREL | Manually annotated from scratch and later manually and partially automatically corrected |
| DEPS | Currently unused |
| MISC | `SpaceAfter` feature added automatically |

Besides reproducing the original text (`# text =`), the headers of each sentence identify it (`# sent_id = `) with a three-letter code representing the literary work they belong to (`DVE` = *De vulgari eloquentia*, `Mon` = *Monarchia*, `Epi` = *Letters*, `Que` = *Questio de aqua et terra*, `Egl` = *Eclogues*) coupled with a progressive key starting from 1, and also display a more precise reference (i.e. book, section, paragraph...) internal to that work by means of a row introduced by `# citation_hierarchy = `.

## Data split

The treebank is split into three subsets, `dev`, `test` and `train`, with an approximate ratio of 20%/20%/60%. Each text in the **UDante** treebank consists of ordered, running text and represents a complete literary work (*De vulgari eloquentia*, *Monarchia*, *Questio de aqua et terra*) or a coherent collection of texts (*Eclogues*, *Letters*): as such, no text has been further split, resulting in a somewhat skewed split ratio with respect to the canonical 10 000 tokens for `dev`/`test` of corpora of comparable magnitude. The distribution of the works with respect to the subsets is as follows:

* `dev`: *Letters* = 11 667 tokens (21%)
* `test`: *De vulgari eloquentia* = 13 493 tokens (24%)
* `train`: *Monarchia* + *Eclogues* + *Questio de aqua et terra* = 22 764 + 2 662 + 5 111 = 30 537 tokens (55%) 

Since the **UDante** treebank represents all known Latin works by Dante, its structure is foreseen to remain quite stable in the future. 



# Changelog

* 2021-05-15 v2.8
    * First release in UD


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.8
License: CC BY-NC-SA 3.0
Includes text: yes
Genre: nonfiction poetry email
Lemmas: converted with corrections
UPOS: converted with corrections
XPOS: manual native
Features: converted with corrections
Relations: manual native
Contributors: Cecchini, Flavio Massimiliano; Moretti, Giovanni; Passarotti, Marco; Sprugnoli, Rachele
Contributing: elsewhere
Contact: flavio.cecchini@unicatt.it
===============================================================================
</pre>

