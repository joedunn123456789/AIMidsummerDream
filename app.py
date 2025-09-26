from flask import Flask, request, jsonify
from textblob import TextBlob
import random

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment = TextBlob(text).sentiment.polarity
    mood = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"

    return jsonify({
        "text": text,
        "sentiment": mood,
        "polarity": sentiment
    })

# --- New Q&A feature ---
QUESTIONS = [
    "What’s your favorite movie?",
    "How do you feel about Mondays?",
    "What’s something that made you smile today?",
    "What frustrates you the most?",
    "Do you enjoy working with technology?"
]

@app.route("/question", methods=["GET"])
def get_question():
    """Return a random question."""
    question = random.choice(QUESTIONS)
    return jsonify({"question": question})

@app.route("/answer", methods=["POST"])
def analyze_answer():
    """Analyze the sentiment of the user’s answer."""
    data = request.get_json()
    if not data or "answer" not in data:
        return jsonify({"error": "No answer provided"}), 400

    text = data["answer"]
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return jsonify({
        "answer": text,
        "sentiment": sentiment,
        "polarity": polarity
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
