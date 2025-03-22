import requests
from gtts import gTTS
from deep_translator import GoogleTranslator
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon if not available
nltk.download('vader_lexicon')

API_KEY = "73f2ca8eaca34ce3a9a53b520f112a3a"
sia = SentimentIntensityAnalyzer()

def get_news(company_name):
    """Fetch news articles for a company"""
    url = f"https://newsapi.org/v2/everything?q={company_name}&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    return None

def analyze_sentiment(articles):
    """Perform sentiment analysis on each article"""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    article_sentiments = []

    for article in articles[:10]:  # Analyzing top 10 articles
        title = article.get("title", "")
        description = article.get("description", "")

        # Get sentiment score using VADER
        sentiment_score = sia.polarity_scores(title + " " + description)
        compound_score = sentiment_score["compound"]

        # Categorize sentiment
        if compound_score >= 0.05:
            sentiment = "Positive"
            sentiment_counts["Positive"] += 1
        elif compound_score <= -0.05:
            sentiment = "Negative"
            sentiment_counts["Negative"] += 1
        else:
            sentiment = "Neutral"
            sentiment_counts["Neutral"] += 1

        article_sentiments.append({
            "title": title,
            "description": description,
            "sentiment": sentiment
        })

    return sentiment_counts, article_sentiments

def get_trending_summary(articles):
    """Return summary of the most trending article"""
    if not articles:
        return "No trending article found."
    return articles[0].get("description", "No summary available.")

def generate_hindi_audio(text):
    """Convert text to Hindi speech"""
    translated_text = GoogleTranslator(source="en", target="hi").translate(text)
    tts = gTTS(text=translated_text, lang="hi")
    filename = "news_summary_hindi.mp3"
    tts.save(filename)
    return filename
