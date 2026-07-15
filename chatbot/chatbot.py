import difflib
import re
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.util import filter_spans
import knowledge_base as k
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# SMTP Configuration Constants
SENDER_EMAIL = "karan.bhatt.bhavnagar@gmail.com"
SENDER_PASSWORD = "pmef abok epcw yrva"
RECEIVER_EMAIL = "theeasylearn@gmail.com"

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

def send_email_with_attachment(file_path):
    smtp_server = "smtp.gmail.com"
    port = 587
    
    subject = f"Chatbot Session Log - {os.path.basename(file_path)}"
    body = "Please find attached the chatbot session log file."
    
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with open(file_path, "r", encoding="utf-8") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(file_path)}",
            )
            msg.attach(part)
            
        print(f"\nBot: [SMTP] Connecting to {smtp_server}:{port}...")
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        
        if SENDER_EMAIL != "your_email@gmail.com" and SENDER_PASSWORD != "your_app_password":
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("Bot: [SMTP] Email sent successfully!")
        else:
            print("Bot: [SMTP] Warning: Default/mock credentials detected. Skipping actual email dispatch.")
            print("Bot: [SMTP] To send real emails, update the constants at the top of chatbot.py.")
        server.quit()
    except Exception as e:
        print(f"Bot: [SMTP] Error sending email: {e}")
        print("Bot: [SMTP] The log file was saved successfully but could not be sent via email.")

if __name__ == '__main__':
    # Chatbot Loop
    start_prompt = "Bot: Hello! I am your EasyLearn Academy assistant."
    print(start_prompt)
    
    prompt_name = "Please enter your full name: "
    fullname = input(prompt_name).strip()
    
    prompt_email = "Please enter your email: "
    email = input(prompt_email).strip()
    
    prompt_mobile = "Please enter your mobile number: "
    mobile = input(prompt_mobile).strip()
    
    # File Setup
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_fullname = "".join([c if (c.isalnum() or c in "._-") else "_" for c in fullname])
    filename = f"{timestamp}_{safe_fullname}.txt"
    
    session_log = f"Full Name: {fullname}\nEmail: {email}\nMobile: {mobile}\n\n--- Conversation Session ---\n"
    
    exit_notice = "Type 'bye' to exit.\n"
    print(exit_notice)
    
    while True:
        prompt_you = "You: "
        question = input(prompt_you).strip()
        
        session_log += f"You: {question}\n"
        
        if question.lower() in ["bye", "exit", "goodbye", "quit"]:
            exit_msg = "Bot: Bye!"
            print(exit_msg)
            session_log += f"Bot: Bye!\n"
            break
        else:
            response = get_response(question)
            print(response)
            session_log += f"{response}\n"
    
    # Sanitize Log Content (replace Unicode bullets and rupee symbols with clean ASCII characters)
    session_log_sanitized = (session_log
                             .replace("•", "- ")
                             .replace("\u2022", "- ")
                             .replace("₹", "Rs. ")
                             .replace("\u20b9", "Rs. "))
    
    # Save Log File
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(session_log_sanitized)
        print(f"\nBot: Chatbot log saved to {filename}")
    except Exception as e:
        print(f"\nBot: Error saving log file: {e}")
    
    # Email the file
    send_email_with_attachment(filename)
