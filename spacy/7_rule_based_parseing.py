import spacy 
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
text = """apple is buying indian startup for $1 billion. Alon Musk is the CEO of Tesla."""

doc = nlp(text)
# ? one or zero occurrence of the preceding token
pattern = [
    {"LOWER": "apple"},
    {"IS_PUNCT": True, "OP": "?"},
    {"LOWER": "is"},
    {"LEMMA": "buy"},
    {"LOWER": "indian"},
    {"IS_PUNCT": True, "OP": "?"},
    {"LOWER": "startup"},
]
matcher.add("Apple_Buying ", [pattern])
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(match_id, start, end, span.text)
print("_"*120)
