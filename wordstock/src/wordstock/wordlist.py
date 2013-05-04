'''
Created on 4 May 2013

Word List utilities
Useful for cheating at crosswords, Scrabble(TM), word puzzles... ;-)

Copyright 2013 Steven Kay

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


'''

from collections import Counter
import time
import re

class wordlist(object):
    
    def __init__(self,file_like_object):
        self.source = file_like_object
        self.words=[]
        start=time.time()
        for line in self.source:
            word = line.rstrip()
            word = word.lower()
            wordset=Counter([x for x in word])
            self.words.append((word,wordset))
        took=time.time()-start
        print "Loaded %d words in %2.4f secs" % (len(self.words),took)

    def _dumpWords(self):
        '''
        debug routine - shows data structure being used
        '''
        for x,y in self.words:
            print "%20s:%s" % (x,y) 
        
    def gather(self,generator_callable):
        '''
        courtesy method to return the results of the given call as a list
        uses more memory but may suit you better
        e.g.
        >>> print mywordlist.gather(mywordlist.anagrams("silos"))
        ['soils']
        '''
        s=[]
        for x in generator_callable:
            s.append(x)
        return s
            
    def wordscontainingall(self,letters):
        ''' 
        yields all words containing all of the given letters, in any order
        '''
        letters=letters.lower()
        sortedletters=sorted(letters)
        letts=Counter([x for x in letters])
        for word,letterset in self.words:
            els = (letterset & letts).elements()
            res = sorted("".join(els))
            if res==sortedletters:
                yield word
                
    def anagrams(self,letters):
        '''
        special case of the wordscontainingall(), passes back only those words using just the 
        letters supplied (so drop any words which are longer than the original)
        '''
        letters=letters.lower()
        lenletters = len(letters)
        for word in self.wordscontainingall(letters):
            if (len(word)==lenletters and word!=letters):
                yield word

    def matching(self,pattern):
        '''
        pattern is a simplified form of regex
        * matches any number of letters
        _ matches one letter
        any other letter should match exactly once
        e.g. 
        *ing - words ending in 'ing'
        p_s__t - words starting p, blank, s, blank, blank, t
        '''
        pattern = pattern.lower()
        patt = pattern.replace("*",".*")
        patt = patt.replace("_","[a-z]")
        patt = "^%s$" % patt
        for word, letterset in self.words:
            if re.match(patt, word):
                yield word
