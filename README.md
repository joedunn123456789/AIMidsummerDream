# AIMidsummerDream 🌙🤖

![CI](https://github.com/joedunn123456789/AIMidsummerDream/actions/workflows/python-app.yml/badge.svg)


> *“The person who says it can’t be done is always interrupted by the one who just did it.”*  
> — Chief Wilson, *Daylight (1996)*

AIMidsummerDream is a lightweight **AI microservice** that analyzes text sentiment.  
It’s designed as a showcase of **AI development, API design, and DevOps skills** — proving that even the “undeliverable” can be delivered.

---

## 🚀 Overview
- Built with **Python + Flask**  
- Exposes a simple `/analyze` endpoint  
- Performs **sentiment analysis** (positive, negative, neutral)  
- Fully **Dockerized** for one‑command deployment  

---

## ✨ Features
- 🔍 Text sentiment analysis using [TextBlob](https://textblob.readthedocs.io/en/dev/)  
- 🐳 Docker support for easy portability  
- ⚡ Minimal setup — run locally or in a container with just a few commands  
- 📖 Clean, recruiter‑friendly documentation  

---

## ⚡ Quickstart

### Clone the repo
```bash
git clone https://github.com/joedunn123456789/AIMidsummerDream.git
cd AIMidsummerDream

pip install -r requirements.txt
python app.py

Visit: http://localhost:5000/analyze

docker build -t aimidsummerdream .
docker run -p 5000:5000 aimidsummerdream 
```
---

## 📜 License
This project is licensed under the MIT License — free to use, modify, and share.

---

## 🙌 Why This Repo?
This project demonstrates:
AI‑first thinking → practical machine learning integration
DevOps awareness → containerization and portability
Creative branding → Shakespearean theme + bold positioning

Because sometimes, the impossible just needs the right developer.

---

## 🛣️ Future Work

| Feature                     | Value to Recruiter                          | Status   |
|-----------------------------|---------------------------------------------|----------|
| ☁️ Cloud Deployment (AWS)   | Shows cloud + DevOps deployment skills      | Planned  |
| 🔄 CI/CD with GitHub Actions| Demonstrates automation + pipeline mastery  | Planned  |
| 🧠 Extra AI Endpoints       | Expands AI versatility (keywords, summary)  | Planned  |
| 📊 Unit Tests + Coverage    | Proves code quality + testing discipline    | Planned  |


