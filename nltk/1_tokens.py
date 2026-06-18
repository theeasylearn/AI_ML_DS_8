import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

#load model
nltk.download('punkt_tab')

text = """Natural Language Processing (NLP) is a branch of Artificial Intelligence that enables computers to understand, interpret, and generate human language. It is widely used in applications such as chatbots, language translation, sentiment analysis, speech recognition, and text summarization. By combining linguistics with machine learning and deep learning techniques, NLP helps machines communicate and interact with humans more effectively.
"""
# print(text)

lines = sent_tokenize(text)
print(lines)

words = word_tokenize(text)
print(words)
