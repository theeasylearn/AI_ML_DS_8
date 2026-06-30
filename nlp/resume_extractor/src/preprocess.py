import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Keep line breaks for better section detection"""
    # Replace multiple spaces with single but keep newlines
    text = re.sub(r' +',' ', text)

    # Replace newlines with single new line
    text = re.sub(r'\n+','\n', text)
    return text

def preprocess_resume(text):
    text = clean_text(text)
    doc = nlp(text)
    return doc