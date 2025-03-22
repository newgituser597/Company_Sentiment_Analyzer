import streamlit as st
import api  # Import the functions from api.py
import matplotlib.pyplot as plt

st.title("📊 Company Sentiment Analysis")

# User Input
company_name = st.text_input("Enter Company Name", "")

if company_name:
    st.write(f"Fetching news for **{company_name}**...")

    # Fetch News Articles
    articles = api.get_news(company_name)

    if articles:
        # Perform Sentiment Analysis
        sentiment_counts, article_sentiments = api.analyze_sentiment(articles)

        # Display Trending Summary
        st.subheader("📢 Trending Article Summary")
        trending_summary = api.get_trending_summary(articles)
        st.write(trending_summary)

        # Generate and Play Hindi Audio
        st.subheader("🔊 Hindi Audio Summary")
        audio_file = api.generate_hindi_audio(trending_summary)
        st.audio(audio_file, format="audio/mp3")

        # Define color mapping for sentiment
        sentiment_colors = {
            "Positive": "green",
            "Negative": "red",
            "Neutral": "blue"
        }

        # Display Sentiment for Each Article
        st.subheader("📰 Articles & Sentiment")
        for i, article in enumerate(article_sentiments):
            st.markdown(f"### {i+1}. {article['title']}")  # Title in larger font
            st.write(article["description"])  # Article description

            # Get the sentiment color
            sentiment = article["sentiment"]
            color = sentiment_colors.get(sentiment, "black")  # Default to black if sentiment is unknown

            # Display sentiment in bold & color
            st.markdown(f"**Sentiment:** <span style='color:{color}; font-weight:bold;'>{sentiment}</span>", unsafe_allow_html=True)

        # Sentiment Pie Chart
        st.subheader("📊 Sentiment Distribution")
        labels = sentiment_counts.keys()
        sizes = sentiment_counts.values()
        colors = ['#81C784', '#E57373', '#64B5F6']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
        ax.set_title(f"Sentiment Distribution for {company_name}")
        st.pyplot(fig)

    else:
        st.write("❌ No news articles found.")
