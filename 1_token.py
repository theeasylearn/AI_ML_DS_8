import spacy as sa 
#load model
nlp = sa.load('en_core_web_sm')
#create doc object 
doc = nlp('I am learning NLP. learning NLP is fun. i am student of machine learning.')
#generate tokens 
count = 0
for token in doc:
    print(token.text)
    count = count + 1
print("total token =",count)

