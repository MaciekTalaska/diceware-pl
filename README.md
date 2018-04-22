Polish diceware list based on list created by Piotr (DrFugazi) Tarnowski.
=========================================================================

Recently I started created a small utility helping creating easy to remember, secure passwords based on the Diceware method. I didn't really like some of the long list I have found. There were a lot of numbers, shortcuts, non-real world words (smileys), or even combination of 2 & 3 letters that are ot meaningful words at all. I had a strong feeling that to make the diceware method work, words used should be easy to remember. Diceware method should make it easier for humans to remember our passwords, so why use "words" that make it harder?

Luckilly I have bumped on interesting article on IFF site (https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) describing process of creating very hand picked list of words. I have downloaded the list (for English) and I think this is the way proper list for diceware should be created.

When I got to the point of adding list of polish words - I couldn't find a list so nicely curated. I decided to make some improvements to the list by Piotr (DrFugazi) Tarnowski.


How is the list built?
----------------------

This list is heavily modified. I have made folling assumptions:
- no words shorter than 4 characters
- no numbers (literals and phonetic description)
- no "artificial" - so no ascii smileys
- no shortcuts (mHz, kHz)
- no names
- no offensive words (I may have missed some, but manual check is a really mundane task...)

Additional requirements:
1. All words should sound and be written like a native polish word - so you will not find such popular words as: lunch (as this one is borrowed from English and for polish speakers it reads different than it should - taking under consideration polish spelling rules) 
2. Words should be simple to remember - so no sophisticad words, no words being very rarely used, no words being used only by small bunch of professionals. The list should be good enough for anyone. 

I decided not to generate dice throws indexes. Mainly due to the fact that I don't find it helpful when using electronically created list. 

**Update:** just for the sake of convenience I have decided to create a simple Python script that takes a text file (assuming that it is a diceware list - i.e. each line is a word) and generates a list with indexes.
Usage:

`./addindexes.py diceware-pl.txt` that will generate `diceware-pl.txt.out` file. Just rename and use it.

Important note
--------------

At the moment the list consists of 5887 words. To select 1 word it is required to throw a dice 5 times (log(5887, base 6) is ~4.84). The number of combinations for 5 rolls of a dices is 5^6 which equals to 7776. The diffence between 6^5 and length of the list is 1889. So... what does that mean? Well it means that using this list right now requires one either to fill it with some additional words (up to the 7776 boundary) or compute the index using mod 5887, which unfortunately means that some words (first 1889) are going to be chosen much more frequently than others.

I am planning to make some further adjustments to the list a bit later. I hope to make it of exactly 6^4 length. 

Help?
-----

If you think that some words should be added/removed - let me know, or just create a pull request.


Some statistics:
----------------

| |My list | List by Piotr (DrFugazi) Tarnowski |
| --- | --- | --- |
| Words | 5887 | 7536 |
| Characters* | 37540 | 44394 |
| Average word length | ~6.4 | ~5.9 |


* computed using: wc -c dicelist-pl.txt


License?
--------

This work is under "do whatever you like" license.
