import os
import uuid
import datetime
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Active session store (in-memory)
sessions = {}

# Enable CORS manually for all responses to allow opening chatbot.html directly via file://
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    return response

def finalize_session(session_id):
    sess = sessions[session_id]
    sess['active'] = False
    
    # Sanitize Log Content (replace Unicode bullets and rupee symbols with clean ASCII characters)
    session_log_sanitized = (sess['session_log']
                             .replace("•", "- ")
                             .replace("\u2022", "- ")
                             .replace("₹", "Rs. ")
                             .replace("\u20b9", "Rs. "))
    
    # Save Log File
    filename = sess['filename']
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(session_log_sanitized)
        print(f"\nServer: Chatbot log saved to {filename}")
    except Exception as e:
        print(f"\nServer: Error saving log file: {e}")
        
    # Email the file using the existing SMTP configuration in chatbot.py
    from chatbot import send_email_with_attachment
    send_email_with_attachment(filename)

@app.route('/')
def index():
    # Serve chatbot.html from the root folder if accessed through the server
    return send_from_directory('.', 'chatbot.html')

@app.route('/api/start', methods=['POST', 'OPTIONS'])
def start_session():
    if request.method == 'OPTIONS':
        return '', 200
        
    data = request.json or {}
    fullname = data.get('fullname', '').strip()
    email = data.get('email', '').strip()
    mobile = data.get('mobile', '').strip()
    
    if not fullname or not email or not mobile:
        return jsonify({'error': 'Full name, email, and mobile number are required to start the chatbot.'}), 400
        
    session_id = uuid.uuid4().hex
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_fullname = "".join([c if (c.isalnum() or c in "._-") else "_" for c in fullname])
    filename = f"{timestamp}_{safe_fullname}.txt"
    
    session_log = f"Full Name: {fullname}\nEmail: {email}\nMobile: {mobile}\n\n--- Conversation Session ---\n"
    
    sessions[session_id] = {
        'fullname': fullname,
        'email': email,
        'mobile': mobile,
        'filename': filename,
        'session_log': session_log,
        'active': True
    }
    
    return jsonify({
        'session_id': session_id,
        'message': 'Chatbot session started.'
    })

@app.route('/api/message', methods=['POST', 'OPTIONS'])
def handle_message():
    if request.method == 'OPTIONS':
        return '', 200
        
    data = request.json or {}
    session_id = data.get('session_id')
    message = data.get('message', '').strip()
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Invalid or expired session. Please start a new chat.'}), 404
        
    sess = sessions[session_id]
    if not sess['active']:
        return jsonify({'error': 'This session has already been closed.'}), 400
        
    # Append message to log
    sess['session_log'] += f"You: {message}\n"
    
    # Check if message is an exit command
    if message.lower() in ["bye", "exit", "goodbye", "quit"]:
        sess['session_log'] += "Bot: Bye!\n"
        finalize_session(session_id)
        return jsonify({
            'response': 'Bot: Bye!',
            'session_ended': True
        })
        
    # Get response from chatbot NLP matcher
    from chatbot import get_response
    response_text = get_response(message)
    sess['session_log'] += f"{response_text}\n"
    
    return jsonify({
        'response': response_text,
        'session_ended': False
    })

@app.route('/api/exit', methods=['POST', 'OPTIONS'])
def end_session():
    if request.method == 'OPTIONS':
        return '', 200
        
    data = request.json or {}
    session_id = data.get('session_id')
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Invalid or expired session.'}), 404
        
    sess = sessions[session_id]
    if sess['active']:
        sess['session_log'] += "Bot: Bye!\n"
        finalize_session(session_id)
        return jsonify({'message': 'Session ended, log saved and emailed.'})
    else:
        return jsonify({'message': 'Session was already closed.'})

if __name__ == '__main__':
    print("Starting EasyLearn Chatbot Web Server on http://127.0.0.1:5000...")
    app.run(host='127.0.0.1', port=5000, debug=True)
