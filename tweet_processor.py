"""
Process tweets and convert to sentiment
"""

import os
import nltk
import csv
import json
import pandas as pd
import tweesmu as tw

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

# TextBlob sentiment analyzer
from textblob import TextBlob

# IBM Watson sentiment analyzer
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

ibm_api_key = os.getenv("ibm_api_key")
ibm_service_endpoint='https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/4d2400c1-25f8-4249-bf7e-2226ba2c2258'
authenticator = IAMAuthenticator(ibm_api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(ibm_service_endpoint)


def processSentiment(file_name):
    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    s = []

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip header row
        next(csv_reader)

        for row in csv_reader:
            try:
                text = tw.processTweet(row[2])
                sentiment = analyzer.polarity_scores(text)
                if sentiment["compound"] == 0.0: continue
                # Watson
                # response = natural_language_understanding.analyze (
                #     text = text,
                #     features = Features(sentiment=SentimentOptions())).get_result()

                s.append({
                    "date": row[0],
                    "text": text,
                    "compound": sentiment["compound"],
                    "positive": sentiment["pos"],
                    "negative": sentiment["neg"],
                    "neutral": sentiment["neu"],
                    "textblob_polarity": TextBlob(text).sentiment.polarity
                    #"watson_score": response.get('sentiment').get('document').get('score')
                })
                
            except Exception as e:
                pass
        
    # Create DataFrame
    return pd.DataFrame(s)

df = processSentiment('./btc_tweets_2020-08-18.csv')

print(df.head(10))
df.to_csv('btc_sentiment_2020-08-18.csv', encoding='utf-8')
print(df.describe())




