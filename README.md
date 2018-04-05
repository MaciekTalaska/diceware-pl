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

Help?
-----

If you think that some words should be added/removed - let me know, or just create a pull request.


Some statistics:
----------------

Number of words: 		5887
Total number of characters*: 	37540
Average word length: 		~6.4  

Stats for the original list:
Number of words:		7536	
Total number of charactes:     44394	
Average word length:		~5.9

| |My list | List by Piotr (DrFugazi) Tarnowski |
| --- | --- | --- |
| Words | 5887 | 7536 |
| Characters | 37540 | 44394 |
| Average word length | ~6.4 | ~5.9 |


* - computed using: wc -c dicelist-pl.txt


License?
--------

This work is under "do whatever you like" license.
