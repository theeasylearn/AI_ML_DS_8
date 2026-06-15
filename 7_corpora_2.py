import nltk
from nltk.corpus import brown

print(brown.categories()) #return list of stories in gutenberg 

news = brown.words(categories='science_fiction')
print("No of words ",len(news))
list = news[0:100]
for item in list:
    print(item,end=' ')
