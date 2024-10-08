import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
df = pd.read_csv('detect.csv')
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    return ' '.join(tokens)
df['email_text'] = df['email_text'].apply(preprocess_text)
sia = SentimentIntensityAnalyzer()
def detect_emotion(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
df['emotion'] = df['email_text'].apply(detect_emotion)
def classify_spam(text):
    if 'buy' in text or 'free' in text or 'click' in text or 'warning' in text:
        return 1
    else:
        return 0
df['spam_pred'] = df['email_text'].apply(classify_spam)
print(df)
