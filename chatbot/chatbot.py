import knowledge_base as k
import spacy 
greetings = [
    "hello", "hi", "hey", "good morning", "good afternoon", "good evening",
    "greetings", "welcome", "howdy", "good day",
    "nice to meet you", "pleased to meet you",
    "how are you?", "how's it going?", "how have you been?",
    "what's up?", "what's new?", "how do you do?",
    "long time no see", "glad to meet you",
    "it's a pleasure to meet you",
    "good to see you", "happy to see you",
    "welcome back", "hope you're doing well",
    "hope you are fine"
]
def preprocess(question):
    global greetings
    doc = nlp(question)
    for token in doc:
        text = token.text.lower()
        if text in greetings:
            print("Bot : Hello nice to meet you.")
        else:
            print("Bot: i am thinking....")
nlp = spacy.load('en_core_web_sm')
while True:
    question = input("You: ")
    question = question.lower()
    if question == "bye":
        print("Bot : Bye. please come again")
        break 
    else:
        preprocess(question)