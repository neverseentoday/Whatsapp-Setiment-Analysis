💬 WhatsApp Sentiment & Emotion Analyzer
https://static.streamlit.io/badges/streamlit_badge_black_white.svg
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/NLP-TextBlob%252BNRCLex-orange
https://img.shields.io/badge/License-MIT-green

<div align="center">
🔍 Uncover the Emotional Pulse of Your WhatsApp Conversations
A powerful NLP-powered web application that analyzes sentiments and emotions in your WhatsApp chats through beautiful, interactive visualizations.

👉 Live Demo · 🚀 Quick Start · 📊 Features

</div>
✨ Features
🎯 Core Analysis
📊 Sentiment Analysis - Classify messages as Positive, Negative, or Neutral using TextBlob

😊 Emotion Detection - Identify 10 different emotions (Joy, Anger, Fear, Trust, etc.) with NRCLex

👥 Participant Analytics - Track engagement and emotional patterns for each group member

📈 Interactive Visualizations - Beautiful charts and graphs for easy insights

🎨 Visual Dashboard
Real-time sentiment distribution

Emotion heatmaps and trends

Participant comparison charts

Downloadable analysis reports

🚀 Tech Stack
Frontend: Streamlit 🎈

NLP: TextBlob + NRCLex 🧠

Visualization: Matplotlib + Seaborn 📊

Data Processing: Pandas 🐼

🎯 Live Demo
👉 Try the Live App Now

Simply upload your WhatsApp export and get instant insights! No registration required.

🛠️ Quick Start
1. Clone & Setup
bash
git clone https://github.com/neverseentoday/whatsapp-sentimental-analysis.git
cd whatsapp-sentimental-analysis
pip install -r requirements.txt
2. Run Locally
bash
streamlit run app.py
3. Export Your WhatsApp Data
Open WhatsApp → Select Chat → ⋮ Menu → Export Chat

Choose "Without Media"

Upload the .txt file to the app

🔧 How It Works
🧠 NLP Pipeline
Data Extraction - Parse WhatsApp export format with regex

Text Preprocessing - Clean and normalize messages, handle emojis

Sentiment Analysis - TextBlob for polarity scoring (-1 to +1)

Emotion Detection - NRCLex for emotional classification

Visualization - Interactive charts and metrics dashboard

📊 Analysis Metrics
Sentiment Scores: Polarity (-1 to +1) and Subjectivity (0 to 1)

Emotion Spectrum: Fear, Anger, Anticipation, Trust, Surprise, Positive, Negative, Sadness, Disgust, Joy

Participant Insights: Message frequency, emotional patterns, engagement levels

🎯 Use Cases
👥 For Group Chats
Understand group dynamics and emotional tone

Identify most positive/negative contributors

Track emotional trends over time

👤 For Personal Analysis
Reflect on your communication style

Monitor your emotional patterns

Improve digital wellbeing

🔬 For Researchers
Analyze conversation patterns

Study emotional contagion in groups

Linguistic analysis of digital communication

🌟 Example Insights
python
📊 Total Messages: 1,247
👥 Participants: 8
😊 Positive Sentiment: 42.3%
😐 Neutral Sentiment: 38.1%
😞 Negative Sentiment: 19.6%

Top Emotions:
1. Trust (23.4%)
2. Joy (18.7%) 
3. Anticipation (15.2%)
📸 Preview
Feature	Description
Sentiment Analysis	Pie charts showing positive/negative/neutral distribution
Emotion Dashboard	Bar charts displaying dominant emotions across conversations
Participant Analytics	Comparison of message counts and sentiment by user
Export Results	Download comprehensive analysis as CSV
🤝 Contributing
We love contributions! Feel free to:

🐛 Report bugs and issues

💡 Suggest new features

🔧 Submit pull requests

📚 Improve documentation

Check out our Issues page to get started.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
TextBlob - For sentiment analysis capabilities

NRCLex - For emotion detection using the NRC Emotion Lexicon

Streamlit - For making web app development incredibly simple

WhatsApp - For providing chat export functionality



<div align="center">
Ready to explore the emotions behind your conversations? 🚀
https://static.streamlit.io/badges/streamlit_badge_black_white.svg
https://img.shields.io/github/stars/neverseentoday/Whatsapp-Sentimental-Analysis?style=social

Unlock the hidden emotional patterns in your WhatsApp chats today!

</div>
