# flask_chat/app.py
from flask import Flask, render_template, request, jsonify
from streamlit_bot.chat import get_response  # Import the get_response function
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_text = get_response(user_message)  # Get response from the Gemini model
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)


# for starting this -> python app.py    