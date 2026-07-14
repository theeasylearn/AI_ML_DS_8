import difflib
import re
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.util import filter_spans
import knowledge_base as k

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Register patterns
for topic_name, data in k.knowledge['topics'].items():
    patterns = [nlp.make_doc(keyword) for keyword in data['keywords']]
    matcher.add(topic_name, patterns)

# Build vocabulary for spelling correction
kb_words = set()
for topic_name, data in k.knowledge['topics'].items():
    for keyword in data['keywords']:
        for word in keyword.lower().split():
            word_clean = word.strip("?,.!")
            if word_clean:
                kb_words.add(word_clean)

greeting_words = {"hello", "hi", "hey", "howdy", "gm", "greetings", "welcome","good morning","good evening"}
for word in greeting_words:
    kb_words.add(word)

def correct_spelling(text):
    if not text:
        return text
    words = text.lower().split()
    corrected_words = []
    for word in words:
        clean_word = word.strip("?,.!")
        if not clean_word:
            corrected_words.append(word)
            continue
        
        if clean_word in kb_words:
            corrected_words.append(word)
        else:
            matches = difflib.get_close_matches(clean_word, list(kb_words), n=1, cutoff=0.8)
            if matches:
                corrected = matches[0]
                if word.endswith("?"):
                    corrected += "?"
                elif word.endswith("."):
                    corrected += "."
                elif word.endswith(","):
                    corrected += ","
                elif word.endswith("!"):
                    corrected += "!"
                corrected_words.append(corrected)
            else:
                corrected_words.append(word)
    return " ".join(corrected_words)

def is_greeting(text):
    if not text:
        return False
    text_lower = text.lower().strip()
    
    # Check multi-word greeting phrases with word boundaries
    greeting_phrases = ["good morning", "good afternoon", "good evening", "how are you", "nice to meet you"]
    for phrase in greeting_phrases:
        if re.search(r'\b' + re.escape(phrase) + r'\b', text_lower):
            return True
            
    # Check single-word greetings against tokenized words (exact match only)
    greeting_words = {"hello", "hi", "hey", "howdy", "gm", "greetings", "welcome"}
    doc = nlp(text_lower)
    return any(token.text in greeting_words for token in doc)

def get_response(question):
    if not question or question.strip() == "":
        return "Bot: I'm here to help!"
    
    # Correct spelling first
    question_corrected = correct_spelling(question)
    
    doc = nlp(question_corrected)
    matches = matcher(doc)
    
    # Filter overlapping matches to keep only the longest spans
    spans = []
    for match_id, start, end in matches:
        span = Span(doc, start, end, label=match_id)
        # If the match is a time-of-day word and is preceded by "good", skip it
        if span.text.lower() in {"morning", "afternoon", "evening"}:
            if start > 0 and doc[start - 1].text.lower() == "good":
                continue
        spans.append(span)
    filtered_spans = filter_spans(spans)
    
    if filtered_spans:
        topic_scores = {}
        for span in filtered_spans:
            topic_name = span.label_
            priority = k.knowledge['topics'][topic_name]['priority']
            
            if topic_name not in topic_scores:
                topic_scores[topic_name] = {'priority': priority, 'count': 0}
            topic_scores[topic_name]['count'] += 1
        
        best_topic = min(
            topic_scores.keys(),
            key=lambda t: (topic_scores[t]['priority'], -topic_scores[t]['count'])
        )
        
        answer = k.knowledge['topics'][best_topic]['answer']
        return f"Bot: {answer}"
    
    # No topic match found, check if it's a greeting
    if is_greeting(question_corrected):
        return "Bot: Hello! Nice to meet you. How can I assist you today?"
        
    return "Bot: Sorry, I didn't understand. Could you rephrase?"
# Chatbot Loop
print("Bot: Hello! I am your EasyLearn Academy assistant.")
print("Type 'bye' to exit.\n")
while True:
    question = input("You: ").strip()
    if question.lower() in ["bye", "exit", "goodbye", "quit"]:
        print("Bot: Bye!")
        break
    else:
        response = get_response(question)
        print(response)