# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import re
import emoji
from textblob import TextBlob
from nrclex import NRCLex
import io
import base64


st.set_page_config(
    page_title="WhatsApp Sentiment & Emotion Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #25D366;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #128C7E;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .stProgress .st-bo {
        background-color: #25D366;
    }
</style>
""", unsafe_allow_html=True)

# Analysis functions 
def load_chat_file(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix == ".txt":
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

def clean_message(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = emoji.replace_emoji(text, replace=' emotion ')
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.strip().lower()
    return text

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
        return {"Emotion_Scores": {}, "Dominant_Emotion": None}

def main():
    # Header
    st.markdown('<h1 class="main-header">💬 WhatsApp Sentiment & Emotion Analyzer</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("📊 Analysis Options")
    st.sidebar.markdown("Upload your WhatsApp chat export file to analyze sentiments and emotions.")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader(
        "Upload WhatsApp Chat File", 
        type=['txt', 'csv'],
        help="Upload your exported WhatsApp chat file (.txt or .csv)"
    )
    
    # Analysis options
    st.sidebar.markdown("---")
    st.sidebar.subheader("Analysis Settings")
    show_raw_data = st.sidebar.checkbox("Show Raw Data", value=False)
    show_emotion_details = st.sidebar.checkbox("Show Emotion Details", value=True)
    
    if uploaded_file is not None:
        try:
            # Save uploaded file temporarily
            file_path = Path(f"temp_{uploaded_file.name}")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            # Show loading spinner
            with st.spinner('Analyzing your chat data... This may take a few moments.'):
                # Load and process data
                df = load_chat_file(file_path)
                
                # Show basic info
                st.success(f"✅ Successfully loaded {len(df)} messages from {len(df['Sender'].unique())} participants")
                
                # Show raw data if requested
                if show_raw_data:
                    st.subheader("📄 Raw Chat Data")
                    st.dataframe(df.head(100), use_container_width=True)
                
                # Clean and analyze
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

                # Fill NAs
                df['Sentiment'] = df['Sentiment'].fillna('neutral')
                df['Dominant_Emotion'] = df['Dominant_Emotion'].fillna('neutral')
            
            # Display overview metrics
            st.markdown("---")
            st.subheader("📈 Overview Metrics")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                total_messages = len(df)
                st.metric("Total Messages", total_messages)
            
            with col2:
                unique_senders = df['Sender'].nunique()
                st.metric("Participants", unique_senders)
            
            with col3:
                positive_percentage = (df['Sentiment'] == 'positive').sum() / len(df) * 100
                st.metric("Positive Messages", f"{positive_percentage:.1f}%")
            
            with col4:
                negative_percentage = (df['Sentiment'] == 'negative').sum() / len(df) * 100
                st.metric("Negative Messages", f"{negative_percentage:.1f}%")
            
            # Visualizations
            st.markdown("---")
            st.subheader("📊 Sentiment Analysis")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Sentiment distribution
                fig, ax = plt.subplots(figsize=(10, 6))
                sentiment_counts = df['Sentiment'].value_counts()
                colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # red, teal, blue
                wedges, texts, autotexts = ax.pie(sentiment_counts.values, labels=sentiment_counts.index, 
                                                autopct='%1.1f%%', colors=colors, startangle=90)
                ax.set_title('Sentiment Distribution', fontsize=16, fontweight='bold')
                plt.setp(autotexts, size=12, weight="bold", color='white')
                st.pyplot(fig)
            
            with col2:
                # Sentiment by sender
                fig, ax = plt.subplots(figsize=(12, 6))
                sentiment_by_sender = pd.crosstab(df['Sender'], df['Sentiment'])
                sentiment_by_sender.plot(kind='bar', ax=ax, color=['#FF6B6B', '#45B7D1', '#4ECDC4'])
                ax.set_title('Sentiment Distribution by Participant', fontsize=16, fontweight='bold')
                ax.set_xlabel('Participant')
                ax.set_ylabel('Number of Messages')
                plt.xticks(rotation=45)
                plt.legend(title='Sentiment')
                plt.tight_layout()
                st.pyplot(fig)
            
            # Emotion Analysis
            st.markdown("---")
            st.subheader("😊 Emotion Analysis")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Dominant emotion distribution
                fig, ax = plt.subplots(figsize=(12, 6))
                emotion_counts = df['Dominant_Emotion'].value_counts().head(10)
                sns.barplot(x=emotion_counts.values, y=emotion_counts.index, ax=ax, palette='viridis')
                ax.set_title('Top 10 Dominant Emotions', fontsize=16, fontweight='bold')
                ax.set_xlabel('Number of Messages')
                ax.set_ylabel('Emotion')
                st.pyplot(fig)
            
            with col2:
                # Emotion by sender
                if len(df['Sender'].unique()) <= 10:  # Only show if reasonable number of senders
                    fig, ax = plt.subplots(figsize=(12, 6))
                    emotion_by_sender = pd.crosstab(df['Sender'], df['Dominant_Emotion'])
                    emotion_by_sender = emotion_by_sender[emotion_counts.index]  # Keep only top emotions
                    emotion_by_sender.plot(kind='bar', stacked=True, ax=ax, cmap='Set3')
                    ax.set_title('Emotion Distribution by Participant', fontsize=16, fontweight='bold')
                    ax.set_xlabel('Participant')
                    ax.set_ylabel('Number of Messages')
                    plt.xticks(rotation=45)
                    plt.legend(title='Emotion', bbox_to_anchor=(1.05, 1), loc='upper left')
                    plt.tight_layout()
                    st.pyplot(fig)
                else:
                    st.info("Too many participants to display emotion distribution chart.")
            
            # Detailed emotion scores
            if show_emotion_details:
                st.markdown("---")
                st.subheader("🔍 Detailed Emotion Analysis")
                
                # Calculate average emotion scores
                emotion_cols = ['fear', 'anger', 'anticipation', 'trust', 'surprise', 
                              'positive', 'negative', 'sadness', 'disgust', 'joy']
                
                emotion_data = []
                for _, row in df.iterrows():
                    if row['Emotion_Scores']:
                        emotion_data.append(row['Emotion_Scores'])
                
                if emotion_data:
                    emotion_df = pd.DataFrame(emotion_data)
                    emotion_df = emotion_df.reindex(columns=emotion_cols, fill_value=0)
                    
                    # Average emotion scores
                    avg_emotions = emotion_df.mean().sort_values(ascending=False)
                    
                    fig, ax = plt.subplots(figsize=(12, 6))
                    avg_emotions.plot(kind='bar', ax=ax, color='skyblue')
                    ax.set_title('Average Emotion Scores', fontsize=16, fontweight='bold')
                    ax.set_ylabel('Average Score')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    st.pyplot(fig)
            
            # Participant Analysis
            st.markdown("---")
            st.subheader("👥 Participant Analysis")
            
            # Top participants by message count
            participant_stats = df['Sender'].value_counts().head(10)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(10, 6))
                participant_stats.plot(kind='bar', ax=ax, color='lightcoral')
                ax.set_title('Top 10 Most Active Participants', fontsize=16, fontweight='bold')
                ax.set_xlabel('Participant')
                ax.set_ylabel('Number of Messages')
                plt.xticks(rotation=45)
                st.pyplot(fig)
            
            with col2:
                # Participant sentiment breakdown
                participant_sentiment = df.groupby('Sender')['Sentiment'].value_counts().unstack(fill_value=0)
                participant_sentiment['Total'] = participant_sentiment.sum(axis=1)
                participant_sentiment = participant_sentiment.sort_values('Total', ascending=False).head(10)
                
                st.dataframe(participant_sentiment[['positive', 'neutral', 'negative']], 
                           use_container_width=True)
            
            # Download results
            st.markdown("---")
            st.subheader("📥 Download Results")
            
            # Convert DataFrame to CSV for download
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Analysis Results as CSV",
                data=csv,
                file_name="whatsapp_sentiment_analysis.csv",
                mime="text/csv",
                help="Download the complete analysis results including sentiments and emotions"
            )
            
            # Clean up temporary file
            file_path.unlink()
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            st.info("""
            **Common issues:**
            - Make sure your WhatsApp chat export is in the correct format
            - For .txt files, ensure the date format matches: MM/DD/YY, HH:MM - Sender: Message
            - For .csv files, ensure there's a 'Message' column
            """)
    
    else:
        # Show instructions when no file is uploaded
        st.markdown("""
        ## 📋 How to Use This Analyzer
        
        1. **Export your WhatsApp chat:**
           - Open the WhatsApp conversation you want to analyze
           - Tap on the three dots (⋮) → More → Export chat
           - Choose "Without Media"
        
        2. **Upload the file:**
           - Use the file uploader in the sidebar
           - Supported formats: .txt (WhatsApp export) or .csv
        
        3. **View analysis:**
           - Sentiment distribution (Positive, Neutral, Negative)
           - Emotion analysis using NRCLex
           - Participant statistics
           - Interactive visualizations
        
        ## 🔍 What We Analyze
        
        - **Sentiment**: Positive, Neutral, Negative messages using TextBlob
        - **Emotions**: Fear, Anger, Joy, Trust, etc. using NRCLex
        - **Participation**: Most active members and their sentiment patterns
        - **Trends**: Overall emotional tone of the conversation
        
        ## 💡 Tips for Best Results
        
        - Use English conversations for most accurate analysis
        - Longer conversations provide better insights
        - The analyzer works best with substantive messages (not just emojis or short replies)
        """)

if __name__ == "__main__":
    main()