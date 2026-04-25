"""
College Enquiry Chatbot - Backend (Flask + NLTK)
St. Philomena College (Autonomous), Puttur
"""

import json
import random
import re
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# ─── NLTK Setup ───────────────────────────────────────────────
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# For hosting environments (Render)
nltk.data.path.append('/opt/render/nltk_data')

app = Flask(__name__, static_folder='.')
CORS(app)

# ─── Load Intents ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTENTS_FILE = os.path.join(BASE_DIR, 'intents.json')

with open(INTENTS_FILE, 'r', encoding='utf-8') as f:
    intents_data = json.load(f)

intents = intents_data['intents']

# ─── NLP ─────────────────────────────────────────────────────
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [stemmer.stem(t) for t in tokens if t not in stop_words and len(t) > 1]
    return tokens

def compute_similarity(user_tokens, pattern_tokens):
    if not pattern_tokens:
        return 0.0
    return len(set(user_tokens) & set(pattern_tokens)) / len(set(pattern_tokens))

def classify_intent(user_input):
    user_tokens = preprocess(user_input)
    if not user_tokens:
        return 'unknown', 0.0

    scores = {}

    for intent in intents:
        if intent['tag'] == 'unknown':
            continue

        best_score = 0.0
        for pattern in intent['patterns']:
            score = compute_similarity(user_tokens, preprocess(pattern))
            best_score = max(best_score, score)

        if best_score > 0:
            scores[intent['tag']] = best_score

    if not scores:
        return 'unknown', 0.0

    best_tag = max(scores, key=scores.get)
    best_score = scores[best_tag]

    return (best_tag, best_score) if best_score >= 0.3 else ('unknown', best_score)

def get_response(tag):
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm unable to process your request right now."

# ─── Routes ──────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    msg = data['message'].strip()

    if not msg:
        return jsonify({'error': 'Empty message'}), 400

    tag, confidence = classify_intent(msg)
    response = get_response(tag)

    return jsonify({
        'response': response,
        'intent': tag,
        'confidence': round(confidence, 3)
    })

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

# ─── Run ─────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print(" SPC Chatbot Running...")
    print("=" * 60)

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)