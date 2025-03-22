## REPORT 
# Sentiment Analysis for Company News 

## Abstract
This project aims to build a web-based application that analyzes sentiment in news articles about a given company. By gathering news from various sources, summarizing key insights, and evaluating sentiment, the application helps users quickly grasp market sentiment. Additionally, it converts the summaries into Hindi speech using text-to-speech (TTS) technology. The project is deployed on Hugging Face Spaces for easy access and testing.

## Introduction
Keeping up with company news is crucial for investors, analysts, and business professionals. However, manually analyzing sentiment across different sources can be overwhelming. This project leverages Natural Language Processing (NLP) to automate sentiment analysis, providing structured insights that allow users to make informed decisions efficiently.

## Project Setup
### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open the provided local or public URL to access the app.

## Methodology
### 1. News Extraction
   - Retrieves articles from sources like Google News API, NewsAPI, and GDELT.
   - Uses web scraping (BeautifulSoup, requests) to collect data from additional sources.
   - Identifies the most trending articles and prioritizes them for analysis.

### 2. Sentiment Analysis
   - Utilizes datasets such as FinancialPhraseBank, Reuters News, and Yahoo Finance.
   - Uses the VADER sentiment analysis model to classify articles as Positive, Negative, or Neutral.

### 3. Comparative Sentiment Analysis
   - Examines sentiment trends across the top 10 articles.
   - Highlights variations in sentiment among different news sources.

### 4. Text Summarization & Hindi TTS
   - Extracts key insights from articles to generate concise summaries.
   - Converts the summaries into Hindi speech using an open-source TTS model for accessibility.

## Model Details
### Summarization Model
- Uses NLP-based extractive and abstractive summarization techniques.
- Implements NLTK for text processing.

### Sentiment Analysis Model
- VADER (Lexicon-based approach) for sentiment classification.

### Text-to-Speech (TTS) Model
- Google Text-to-Speech (gTTS) for converting text summaries into Hindi speech.

## API Development
- APIs are developed using Flask to efficiently handle requests.
- The API endpoints support retrieving news, analyzing sentiment, and generating summaries.
- Example API request using Postman or cURL:
   ```bash
   curl -X GET "http://localhost:8000/sentiment?company=Tesla"
   ```

## API Usage
- Google News API / NewsAPI / GDELT: Fetches the latest company-related news.
- VADER (NLTK): Performs sentiment analysis.
- gTTS (Google Text-to-Speech API): Converts summaries into Hindi speech.

## Implementation
### Tech Stack
- Backend: Python with NLP libraries (NLTK, BeautifulSoup, requests).
- Frontend: Streamlit for an interactive user interface.
- Deployment: Hosted on Hugging Face Spaces for easy access.
- Data Handling: Uses API requests and JSON to fetch and process news articles.

### Workflow
1. The user enters a company name.
2. The system fetches relevant news articles.
3. Each article undergoes sentiment analysis.
4. The most trending article's summary and sentiment are displayed first.
5. Hindi TTS generates an audio output of the summary.

## Results & Observations
- The sentiment analysis model effectively classifies articles, but it can struggle with mixed sentiments in financial news.
- VADER works well for general sentiment classification but may not fully capture financial-specific nuances.
- The Hindi TTS feature enhances accessibility for non-English speakers.

## Challenges & Future Scope
- Improving accuracy by integrating specialized financial datasets.
- Enhancing news extraction from JavaScript-heavy websites.
- Speeding up real-time data fetching and processing.
- Exploring additional TTS models for better voice quality.

## Conclusion
This project demonstrates the power of NLP in financial sentiment analysis. By integrating real-time news extraction, sentiment classification, and Hindi TTS, it provides a comprehensive tool for analyzing financial news sentiment. Future updates will focus on improving accuracy, expanding language support, and optimizing performance.

## References
- Kaggle-FinancialPhraseBank
- Google News API, NewsAPI
- VADER NLP model (NLTK)
- Streamlit, Hugging Face Spaces

