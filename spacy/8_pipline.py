import spacy 
nlp = spacy.load('en_core_web_sm')
for name, component in nlp.pipeline:
    print(f"{name:30}: {component}")
print("_"*120)
