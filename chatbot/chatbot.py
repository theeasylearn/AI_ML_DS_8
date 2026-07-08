import spacy
import knowledge_base as k   # Uncomment when you create this file

greetings = [
    "hello", "hi", "hey", "good morning", "good afternoon", "good evening",
    "greetings", "welcome", "howdy", "good day","morning","gm"
    "nice to meet you", "pleased to meet you",
    "how are you?", "how's it going?", "how have you been?",
    "what's up?", "what's new?", "how do you do?",
    "long time no see", "glad to meet you",
    "it's a pleasure to meet you",
    "good to see you", "happy to see you",
    "welcome back", "hope you're doing well",
    "hope you are fine"
]

nlp = spacy.load('en_core_web_sm')

def is_greeting(text):
    """Check if user input contains any greeting (handles single + multi-word)"""
    text = text.lower().strip()
    
    # Remove punctuation so "how are you?" or good morning...  matches "how are you" or good morning
    list = []
    for ch in text:
        if ch.isalnum() or ch.isspace():
            list.append(ch)
    clean_question = ''.join(list)      
    # print(clean_question)
    if clean_question in greetings:
            return True
    return False

def preprocess(question):
    if is_greeting(question):
        print("Bot : Hello nice to meet you.")
    else:
        doc = nlp(question)
        for token in doc:
            for topic in k.knowledge['topics']:
                for item in k.knowledge['topics'][topic]:
                    if item == "keywords":
                        for key in k.knowledge['topics'][topic]['keywords']:
                            #print(token,key)
                            if token.text == key:
                                print(k.knowledge['topics'][topic]['answer'])
                                return None

       

# ==================== Chatbot Loop ====================
print("Bot: Hello! I am your assistant. Type 'bye' to exit.\n")

while True:
    question = input("You: ")
    q_lower = question.lower().strip()
    
    if q_lower == "bye":
        print("Bot : Bye. Please come again!")
        break
    else:
        preprocess(question)