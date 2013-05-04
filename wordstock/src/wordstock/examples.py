'''
Created on 4 May 2013

Examples of using the wordlist functions

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

from wordlist import *

# set up dictionary
# this will only work in Linux
# If you're using Windows, you'll need
# to source your own word list file
# (text file, one word per line, case insensitive)

fi=open(r"/usr/share/dict/words","r")
w=wordlist(fi)
fi.close()

# words contain each vowel, but only once

for word in w.wordscontainingall("AEiou"):
    print word
print "="*80    
 
# words containing the letter a 3 times and a single b

for word in w.wordscontainingall("aAAb"):
    print word
print "="*80    
 
# anagrams of 'team'
 
for word in w.anagrams("tEaM"):
    print word
print "="*80
 
# words starting with s, any number of letters, and ending with -ing 

for word in w.matching("s*iNG"):
    print word
print "="*80
 
# words starting with two unknown letters, followed by 'sign' and any number of letters after that
  
for word in w.matching("__siGn*"):
    print word
print "="*80

# example using gather() wrapper to convert generator output to a list

print w.gather(w.anagrams("sILos"))
print "="*80

