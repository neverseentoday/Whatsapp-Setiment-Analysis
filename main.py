# main.py
# WhatsApp Sentiment & Emotion Analyzer
# Author: Alvin — NLP Project (TextBlob + NRCLex)

import re
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for Windows GUI plotting
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from nrclex import NRCLex
import emoji
from pathlib import Path


# --------------- FILE SETUP -----------------
CHAT_PATH = Path("data/chat2.txt")
print("Starting analysis...")



#loading
def load_chat_file(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Reading {file_path} ...")

    if file_path.suffix == ".txt":
        #pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}),?s*(\d{1,2}:\d{2}) - ([^:]+): (.*)'
        pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}),?\s*(\d{1,2}:\d{2}\s*(?:AM|PM)?)[\s\-]+([^:]+): (.*)'

        rows = []

        with open(file_path, encoding='utf-8') as f:
            for line in f:
                match = re.match(pattern, line)
                if match:
                    rows.append(match.groups())

        df = pd.DataFrame(rows, columns=['Date', 'Time', 'Sender', 'Message'])

    elif file_path.suffix == ".csv":
        df = pd.read_csv(file_path)
        if 'Message' not in df.columns:
            raise KeyError("CSV must contain a column named 'Message'.")
    else:
        raise ValueError("File must be either .txt or .csv format.")
    return df


#cleaning
def clean_message(text):
    if pd.isna(text):
        return ""
    text = str(text)
    # Optionally replace emojis with text description for emotion hints
    text = emoji.replace_emoji(text, replace=' emotion ')
    text = re.sub(r'http\S+', '', text)   # remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # keep letters and spaces only
    text = text.strip().lower()
    return text



#analysis
def analyze_sentiment(text):
    if not text or not isinstance(text, str):
        return [None, None, None]

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return [polarity, subjectivity, sentiment]



def detect_emotion(text):
    if not text or not isinstance(text, str):
        return {"Emotion_Scores": {}, "Dominant_Emotion": None}

    try:
        emotion = NRCLex(text)
        scores = emotion.raw_emotion_scores
        top = emotion.top_emotions
        dominant = top[0][0] if top else "neutral"
        return {"Emotion_Scores": scores, "Dominant_Emotion": dominant}
    except Exception as e:
        print(f"Error extracting emotion: {e}")
        return {"Emotion_Scores": {}, "Dominant_Emotion": None}



def main():
    df = load_chat_file(CHAT_PATH)

    # Clean text
    df['Cleaned_Message'] = df['Message'].apply(clean_message)

    # Sentiment analysis
    sentiment_data = df['Cleaned_Message'].apply(analyze_sentiment).tolist()
    df[['Polarity', 'Subjectivity', 'Sentiment']] = pd.DataFrame(
        sentiment_data, columns=['Polarity', 'Subjectivity', 'Sentiment'], index=df.index
    )

    # Emotion detection
    emotions = df['Cleaned_Message'].apply(detect_emotion)
    df['Emotion_Scores'] = emotions.apply(lambda x: x['Emotion_Scores'])
    df['Dominant_Emotion'] = emotions.apply(lambda x: x['Dominant_Emotion'])

    # Fill Nans for plotting
    df['Sentiment'] = df['Sentiment'].fillna('neutral')
    df['Dominant_Emotion'] = df['Dominant_Emotion'].fillna('neutral')

    # Save results
    out_path = Path("outputs/whatsapp_sentiment_emotion_results.csv")
    out_path.parent.mkdir(exist_ok=True, parents=True)
    df.to_csv(out_path, index=False)
    print(f"✅ Results saved to {out_path.absolute()}")

    # Print preview
    print("\nSample output:")
    print(df[['Sender', 'Message', 'Sentiment', 'Dominant_Emotion']].head(10))

    # Visualization
    print("\nGenerating Sentiment Distribution Plot...")
    plt.figure(figsize=(10, 4))
    sns.countplot(data=df, x='Sentiment', palette='coolwarm')
    plt.title('Sentiment Distribution')
    plt.show()

    print("\nGenerating Dominant Emotion Distribution Plot...")
    plt.figure(figsize=(10, 4))
    sns.countplot(data=df, x='Dominant_Emotion', palette='mako')
    plt.title('Dominant Emotion Distribution')
    plt.xticks(rotation=45)
    plt.show()

print("Analysis complete.")
if __name__ == "__main__":
    main()
