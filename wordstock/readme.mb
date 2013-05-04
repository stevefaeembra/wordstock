What it does
============

Wordstock is a simple application in Python for handling long lists of words.
You can use it to cheat at Scrabble(TM), find crossword clues and anagrams.

PREREQUISITES
=============

You will need a word list file. For copyright reasons this is not included, you'll need to find your own.

This file is assumed :-
- to be a text file, one word per line.
- it doesn't have to be sorted, but it'll help if you want the output to be sorted ;-)
- case insensitive - the words are converted to lower case on input
- method calls are also case-insensitive

You can find many such files on the Internet. 
Search for "TWL06.txt" for a good example (178k words).

If running Linux, you can always try using the password dictionary file (/usr/share/dict/words)

Getting Started
===============

First, set up the dictionary. You pass in a file-like object, e.g.

fi=open(r"/usr/share/dict/words","r")
w=wordlist(fi)
fi.close()

Methods
=======
All methods are generators, for example

for word in w.anagrams("tEaM"):
    print word
    
However, if you'd rather have a list, you can call the gather() method to wrap the
function call, which returns a list. This takes up more memory than the generator, so you
should use with caution if you're likely to return LOTS of words.

list = w.gather(w.anagrams("sILos"))
print list

