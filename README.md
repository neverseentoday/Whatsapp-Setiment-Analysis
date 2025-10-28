🧠 WhatsApp Sentiment & Emotion Analyzer

Perform Sentiment Analysis and Emotion Detection on WhatsApp chat data using NLP, TextBlob, and NRCLex — uncovering how people express emotions in digital communication.

📖 Overview

WhatsApp is one of the most widely used communication platforms — a goldmine for understanding human emotions and social interactions.
This project transforms exported WhatsApp messages into emotional insights through advanced text analysis.

It automatically identifies:

🟢 Sentiment Polarity: Positive, Negative, or Neutral

😊 Dominant Emotions: Joy, Anger, Fear, Trust, Sadness, etc.

👥 Participant Insights: Mood trends, message frequency & engagement levels

Using TextBlob for sentiment scoring and NRCLex for emotion detection, the system converts plain conversations into rich emotional analytics — with interactive visualizations and exportable reports.

✨ Features

🎯 Core Analysis

📊 Sentiment Analysis: Classify messages as Positive, Negative, or Neutral

😊 Emotion Detection: Identify up to 10 emotions (Joy, Anger, Fear, Trust, Anticipation, etc.)

👥 Participant Analytics: Track engagement and mood variations per user

📈 Interactive Visualizations: Sentiment charts, emotion heatmaps, and user comparisons

🎨 Visual Dashboard

Real-time sentiment distribution

Emotion trends and participant comparisons

Downloadable analysis reports

🧩 Tech Stack

Language: Python 3.10+

Libraries Used:

🐼 pandas – Data processing

🧠 textblob – Sentiment analysis (polarity & subjectivity)

💬 nrclex – Emotion detection

😄 emoji – Emoji preprocessing

📊 matplotlib + seaborn – Visualizations

🎈 (Optional) Streamlit – Interactive dashboard interface

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/neverseentoday/Whatsapp-Sentiment-Analysis.git
cd whatsapp-sentiment-analysis

2️⃣ Setup Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt
python -m textblob.download_corpora

4️⃣ Add WhatsApp Chat File

Export any chat from WhatsApp:

Open Chat → ⋮ Menu → Export Chat → Choose “Without Media”

Place the exported .txt or .csv file in the data/ folder (e.g., data/chat.txt).

Example format:

12/07/2025, 09:31 - Me: Feeling excited for the trip tomorrow.
12/07/2025, 09:33 - John: I’m a bit nervous about the weather.

5️⃣ Run the Project
python main.py

📊 Output

CSV Report:

outputs/whatsapp_sentiment_emotion_results.csv


Visuals Generated:

Sentiment Distribution (Positive / Negative / Neutral)

Emotion Spectrum (Joy, Fear, Anger, Trust, Sadness, etc.)

Example Result:

Sender	Message	Sentiment	Dominant_Emotion
John	Hey good morning!	Positive	Joy
Me	Feeling super excited!	Positive	Joy
John	I'm a bit nervous though.	Negative	Fear
Me	Don't worry everything will go great!	Positive	Trust
🧠 How It Works
🔧 NLP Pipeline

Data Extraction: Parse WhatsApp export format using regex.

Text Preprocessing: Clean text, remove links, emojis, and special characters.

Sentiment Analysis: Compute polarity & subjectivity with TextBlob.

Emotion Detection: Classify emotions using NRCLex lexicon.

Visualization: Display charts and metrics using Matplotlib & Seaborn.

💡 Use Cases

👥 Group Analysis: Understand group dynamics and emotional tone.
👤 Personal Reflection: Track your communication mood and positivity.
📊 Research: Study emotional contagion, tone, and language trends in social conversations.
💬 Business/Support: Monitor sentiment in customer communications.

🧪 Future Enhancements

🚀 Integrate BERT/RoBERTa for deeper emotion classification
🎈 Add Streamlit Dashboard for real-time interaction
🧩 Include emoji-based emotion weighting
📉 Enable cross-user emotion comparison analytics

🤝 Contributing

We welcome all contributions!

🐛 Report bugs or suggest features

🔧 Submit pull requests

📚 Improve documentation

Check the Issues
 page to get started.

📜 License

This project is licensed under the MIT License — you’re free to use, modify, and distribute it with proper attribution.

👨‍💻 Author

Alvin Joseph
AI & NLP Enthusiast
📧 iamalvinnjoseph@gmail.com
