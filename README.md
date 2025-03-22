---
title: Company Sentiment Analyzer  
emoji: 📊  
colorFrom: blue  
colorTo: purple  
sdk: streamlit  
sdk_version: "1.30.0"  
app_file: app.py  
pinned: false  
---
# 📊 Company Sentiment Analyzer  

This is a web-based application that analyzes news articles about a company, extracts key insights, and provides a structured sentiment report with text and audio output.  

## Features  
-- Fetches real-time news articles.  
-- Performs sentiment analysis (Positive, Negative, Neutral).  
-- Highlights key topics from articles.  
-- Provides comparative sentiment trends across multiple articles.  
-- Converts  Trending article summaries into Hindi speech.  


## Setup Instructions  

1️⃣ Installation 
Make sure you have **Python 3.8+** installed. Then, install the required dependencies:  

bash
pip install -r requirements.txt

2️⃣ Running the Application
To start the application, run the following command in the project folder:

bash
streamlit run app.py

This will launch the web app in your browser.

# Usage Instructions:

-->>How to Run 

1.Enter a company name in the input box.
2.The app fetches real-time news related to the company.
3.It analyzes sentiment and extracts key insights.
4.View the sentiment trends and key topics from articles.
5.Listen to the Hindi audio summary of the top article.

# Dependencies:

- `streamlit`  
- `requests`  
- `gtts`  
- `deep-translator`  
- `nltk`  
- `matplotlib` 

## Live Demo  
https://huggingface.co/spaces/MadeehaFathima/Company_sentiment_analyzer