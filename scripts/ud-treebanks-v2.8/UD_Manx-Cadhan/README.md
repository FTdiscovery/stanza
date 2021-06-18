
# Summary

This is the Cadhan Aonair UD treebank for Manx Gaelic,
created by Kevin Scannell.

# Introduction

The sentences in the treebank all come from a large web-crawled
corpus of Manx consisting of more than 8M words of text.
This corpus was segmented by sentences, shuffled, and then
300 random sentences were chosen to be tagged.
I believe that the web corpus is nearly comprehensive, which is to say
it contains virtually all non-trivial Manx language texts on the open web.
Therefore, the UD corpus is as close as possible to a “random sample”
of Manx on the web. As such,
[the Bible](http://bible.learnmanx.com/) is heavily represented,
but there are also quite a few sentences from modern sources such as the
[Manx Wikipedia](https://gv.wikipedia.org/),
news stories from
[Manx Radio](https://www.manxradio.com/),
blog posts,
translations of literature, etc.

All POS tags and dependency annotations in the initial release
were added manually. The upstream source code and datasets supporting
the treebank can be found [here](https://github.com/kscanne/gaelg).

Since there are only about 6k words total, we have not 
performed a split into train/dev/test sets, following
[the recommendation](https://universaldependencies.org/release_checklist.html#data-split)
of the UD maintainers.

# Acknowledgments

I created the treebank while visiting Acadamh na hOllscolaíochta Gaeilge
in Carna, Co. na Gaillimhe as a Fulbright Scholar. All of the work was
done during the COVID-19 lockdown in Ireland.

I am grateful to the staff at the Acadamh in Carna for their hospitality
during my visit, to the Fulbright Program for the financial support
which made it possible, and to Saint Louis University for a
much-needed sabbatical leave.

Thanks also to Teresa Lynn and Colin Batchelor for their work on the 
Irish and Scottish Gaelic treebanks, respectively. Since all three
Goidelic languages are grammatically very similar, I was able to
consult their work when deciding how to resolve tricky annotation problems.

# Changelog

* 2020-11-15 v2.7
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.7
License: GNU GPL 3.0
Includes text: yes
Genre: news fiction nonfiction blog social wiki web bible
Lemmas: manual native
UPOS: manual native
XPOS: manual native
Features: manual native
Relations: manual native
Contributors: Scannell, Kevin
Contributing: elsewhere
Contact: kscanne@gmail.com
===============================================================================
</pre>
