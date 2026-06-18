import nltk

# download all corpora 
# nltk.download('all')

from nltk.corpus import gutenberg
from nltk.corpus import brown

print(gutenberg.fileids()) #return list of stories in gutenberg 

whiteman = gutenberg.words('whitman-leaves.txt')
print("No of words ",len(whiteman))
print(whiteman[0:100])
