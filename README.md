Polish diceware list
====================

**Important note:** this list is created based on the list origianlly created by Piotr (DrFugazi) Tarnowski. This list is only available via [webarchive](https://web.archive.org/web/20080926125905/http://www.drfugazi.eu.org/diceware).



Why?
----

Recently I started creating a small utility helping creating easy to remember, secure passwords based on the Diceware method. I didn't really like some of the long list I have found. There were a lot of numbers, shortcuts, non-real world words (smileys), or even combination of 2 & 3 letters that are ot meaningful words at all. I had a strong feeling that to make the diceware method work, words used should be easy to remember. Diceware method should make it easier for humans to remember our passwords, so why use "words" that make it harder?

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
- words should be easy to remember / visualize (have a look at the great xkcd comic strip: https://xkcd.com/936/)

Additional requirements:
1. All words should sound and be written like a native polish word - so you will not find such popular words as: lunch (as this one is borrowed from English and for polish speakers it reads different than it should - taking under consideration polish spelling rules) 
2. Words should be simple to remember - so no sophisticad words, no words being very rarely used, no words being used only by small bunch of professionals. The list should be good enough for anyone. 

Indexes:
--------

**Update:** My list has no index for dice rolls. Just for the sake of convenience I have decided to create a simple Python script that takes a text file (assuming that it is a diceware list - i.e. each line is a word) and generates a list with indexes.

Usage:

`./addindexes.py diceware-pl.txt` or (`python addindexes.py diceware-pl.txt`) generates `diceware-pl.txt.out` file. Just rename and use it.
Please be aware that the script was just a quick hack, so there is no proper error handling etc.

Important note on security, probability of words in regards to list size etc.
-----------------------------------------------------------------------------

There are two factors that influence the "randomeness" of generated password:

1) random generator used- this is simple - there are some very quick pseudo-random number generators. These are often called "insecure" or not "crypto secure" rrandom number generators. There is also another class of solutions - being called cryptographically secure random number generators (https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator). 

2) length of the word list. The original list required 5 dice rolls to generate one word - the list consisted of 6^5 (7776) words in total. At some later point in time I have ended up with a list of size 5887, which still required five dice roll (log(5887, base 6) ~ 4.84). The difference between 7776 and 5887 was 1889, so a generated number (up to 6^5) mod 5887 resulted in first 1889 words having higher probability of being chosen than the rest of the words from the list. That is not really acceptable. 

I have made some efforts to shrink the list a bit further, down to 3888, which is equivalent of 6^5/2.  

Any generated index (up to 6^4) mod 3888 results in each word having the same probability of being chosen as a part of generated password.

Help?
-----

If you think that some words should be added/removed - let me know, or just create a pull request.


Some statistics:
----------------

| | my list | original list |
| --- | --- | --- |
| Words | 3888 | 7536 |
| Characters (`wc -c diceware-pl.txt` ) | 24653 | 44394 |
| Average word length | ~6.3 | ~5.9 |


License?
--------

This work us under [MIT license](https://opensource.org/licenses/mit-license.php).
