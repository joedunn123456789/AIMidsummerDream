from flask import Flask, request, jsonify
from textblob import TextBlob

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
