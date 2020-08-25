"""
Library to support tweet processing
"""

import os
import twitter
import csv
import time
import string
import re

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords 
# nltk.download('stopwords')

# initialize api instance
twitter_api = twitter.Api(consumer_key=os.getenv("twitter_consumer_key"),
                        consumer_secret=os.getenv("twitter_consumer_secret"),
                        access_token_key=os.getenv("twitter_access_token_key"),
                        access_token_secret=os.getenv("twitter_access_token_secret"))

# initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# set stopwords
stopwords = set(stopwords.words('english') + list(string.punctuation) + ['AT_USER','URL', 'rt'])

# process the tweet
def processTweet(tweet):
    tweet = tweet.lower() # convert text to lower-case
    tweet = tweet.encode('ascii', 'ignore').decode('ascii') # remove emojis
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
    words = word_tokenize(tweet) # remove repeated characters (helloooooooo into hello)
    lem = [lemmatizer.lemmatize(word) for word in words]
    output = [word for word in lem if word not in stopwords]
    return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in output]).strip()

# use twitter API to gather tweets
def getTweets(search_keyword, count):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=count, result_type="recent")
        return [{"id":status.id_str, "date": status.created_at, "text":status.text} for status in tweets_fetched]
    except:
        return None