# AIMidsummerDream

AIMidsummerDream is a lightweight AI microservice built with Python and Flask.  
It provides sentiment analysis and a simple Q&A feature.

---

## Overview
- Built with Python 3 and Flask
- Endpoints: /analyze, /question, /answer
- Uses TextBlob for sentiment analysis
- Can run locally or in Docker

---

## API Endpoints

POST /analyze  
Analyze sentiment of given text.  
Example request body: {"text": "I love this project"}

GET /question  
Returns a random question.

POST /answer  
Analyze sentiment of your answer.  
Example request body: {"answer": "I hate Mondays"}

---

## Quickstart

Clone the repo:
git clone https://github.com/joedunn123456789/AIMidsummerDream.git
cd AIMidsummerDream

Install dependencies:
pip install -r requirements.txt

Run locally:
python app.py

Visit:
http://localhost:5000/analyze (POST)
http://localhost:5000/question (GET)
http://localhost:5000/answer (POST)

Run with Docker:
docker build -t aimidsummerdream .
docker run -p 5000:5000 aimidsummerdream

---

## License
MIT License
