import spacy
from spacy.matcher import PhraseMatcher
import knowledge_base as k

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Register patterns
for topic_name, data in k.knowledge['topics'].items():
    patterns = [nlp.make_doc(keyword) for keyword in data['keywords']]
    matcher.add(topic_name, patterns)

def is_greeting(text):
    if not text:
        return False
    text_lower = text.lower().strip()
    greetings = {"hello", "hi", "hey", "howdy", "gm", "greetings", "welcome", "good morning", "good afternoon", "good evening", "how are you", "nice to meet you"}
    if any(g in text_lower for g in greetings):
        return True
    doc = nlp(text_lower)
    greeting_words = {"hello", "hi", "hey", "howdy", "gm", "welcome", "morning", "afternoon", "evening"}
    return any(token.text in greeting_words for token in doc)

def get_response(question):
    if not question or question.strip() == "":
        return "Bot: I'm here to help!"
    
    if is_greeting(question):
        return "Bot: Hello! Nice to meet you. How can I assist you today?"
    
    doc = nlp(question)
    matches = matcher(doc)
    
    if not matches:
        return "Bot: Sorry, I didn't understand. Could you rephrase?"
    
    topic_scores = {}
    for match_id, start, end in matches:
        topic_name = nlp.vocab.strings[match_id]
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