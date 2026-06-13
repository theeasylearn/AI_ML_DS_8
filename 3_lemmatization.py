from nltk.stem import WordNetLemmatizer 

#create object 
lemma = WordNetLemmatizer()

print("Lemmtization of swimming ",lemma.lemmatize('swimming',pos='v'))
print("Lemmtization of reading ",lemma.lemmatize('reading',pos='v'))
print("Lemmtization of dancing ",lemma.lemmatize('dancing',pos='v'))

#adjective 
print("Lemmtization of better ",lemma.lemmatize('better',pos='a'))
print("Lemmtization of quickly ",lemma.lemmatize('quick',pos='a'))
print("Lemmtization of sincerely ",lemma.lemmatize('sincerely',pos='a'))


