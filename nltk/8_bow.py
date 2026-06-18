from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "The cat chased the mouse",
    "The dog chased the cat"
]
cvt = CountVectorizer()

result = cvt.fit_transform(documents)

print("Vocab =",cvt.vocabulary_)

print(result.toarray())