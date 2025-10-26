# Whatsapp-Setiment-Analysis
🧠 WhatsApp Sentiment &amp; Emotion Analyzer Perform Sentiment Analysis and Emotion Detection on WhatsApp chat data using NLP techniques, TextBlob, and NRCLex. This project helps uncover how people express emotions in digital communication by analyzing exported WhatsApp messages.
📖 Overview
WhatsApp has become one of the most widely used platforms for digital communication — making it a valuable source for understanding emotional and social interactions.
This project processes chat exports (.txt or .csv) to identify:

Sentiment polarity (Positive, Negative, Neutral)

Dominant underlying emotions (Joy, Anger, Fear, Trust, Sadness, etc.)

Overall group mood trends and user interaction patterns

Using TextBlob for sentiment scoring and NRCLex for emotion detection, the system converts ordinary WhatsApp messages into insightful emotional analytics with visualizations.

⚙️ Features
✅ Import WhatsApp chat exports (.txt or .csv)
✅ Clean text (remove links, symbols, emojis, numbers)
✅ Perform sentiment classification
✅ Detect dominant emotions using NRCLex lexicon
✅ Generate visual charts for Sentiments and Emotions
✅ Output CSV report for further NLP analysis or dashboards

🧩 Tech Stack
Python 3.10+

Libraries:

pandas – Data handling

textblob – Sentiment analysis (polarity & subjectivity)

nrclex – Emotion detection

emoji – Emoji handling

seaborn + matplotlib – Visualizations

🚀 Getting Started
1. Clone the Repository
bash
git clone (https://github.com/neverseentoday/Whatsapp-Setiment-Analysis.git)
cd whatsapp-sentiment-analysis
2. Setup Virtual Environment
bash
python -m venv venv
venv\Scripts\activate    # (Windows)
source venv/bin/activate # (Mac/Linux)
3. Install Dependencies
bash
pip install -r requirements.txt
python -m textblob.download_corpora
4. Add WhatsApp Chat File
Place your exported file into the data/ folder as chat.txt (or whatsapp_chat.csv).
Format example:

text
12/07/2025, 09:31 - Me: Feeling excited for the trip tomorrow.
12/07/2025, 09:33 - John: I’m a bit nervous about the weather.
5. Run the Project
bash
python main.py
📊 Output
A detailed CSV report saved at:

text
outputs/whatsapp_sentiment_emotion_results.csv
Two visualizations:

Sentiment Distribution – Positive vs. Negative vs. Neutral

Dominant Emotions – Joy, Fear, Anger, Trust, Sadness, etc.

Example preview:

text
Sender,Message,Sentiment,Dominant_Emotion
John,"Hey good morning!",positive,joy
Me,"Feeling super excited!",positive,joy
John,"I'm a bit nervous though.",negative,fear
Me,"Don't worry everything will go great!",positive,trust
📁 Project Structure
text
Whatsapp-Sentiment-Analysis/
│
├── data/                      # Chat exports go here (.txt or .csv)
├── outputs/                   # CSV & visualizations
├── main.py                    # Main Python script
├── requirements.txt            # Dependencies
└── README.md                  # Project documentation
🧠 Key Concepts
TextBlob: Determines message polarity & subjectivity.
NRCLex: Maps words to eight primary emotions — joy, trust, fear, anger, sadness, disgust, surprise, anticipation.

These outputs are combined to provide rich insights into communication tone, emotional diversity, and personal or group-level sentiment dynamics.

💡 Use Cases
Team communication pattern analysis

Group mood tracking

Social media conversation research

Customer support sentiment monitoring

Comparative studies of conversational tone

🧾 Example Visualizations
Sentiment Distribution:
Shows conversation positivity balance.
Emotion Distribution:
Highlights most common emotion types in group chat.

Both are automatically displayed upon execution.

🧪 Future Enhancements
Integrate machine learning emotion classification (BERT or RoBERTa)

Add Streamlit dashboard for real-time chat exploration

Cross-user emotion comparison analytics

Emoji-based emotion weighting

🙌 Contributing
Contributions are welcome! Feel free to fork the project and submit pull requests with enhancements.

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it with attribution.

👨‍💻 Author
Alvin
AI & NLP Enthusiast
📧 Contact: [iamalvinnjoseph@gmail.com]
