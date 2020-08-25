"""
Downloads tweets for a given day
"""

import os
import pandas as pd
import tweepy as tw

# Get credentials for OAuth authentication
consumer_key = os.getenv("twitter_consumer_key")
consumer_secret = os.getenv("twitter_consumer_secret")
access_token = os.getenv("twitter_access_token_key")
access_token_secret = os.getenv("twitter_access_token_secret")
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Search Key word and search dates
search_keyword = 'Bitcoin'
date_since = '2020-08-19'
date_until = '2020-08-20'

# Use tweepy to get around rate limiting
tweets_fetched = tw.Cursor(api.search,
                   q=search_keyword,
                   lang="en",
                   since=date_since,
                   until=date_until
                   ).items()

# process tweets
tweets = []
for status in tweets_fetched:
    try:
        tweets.append({
            "date": status.created_at,
            "id": status.id_str,
            "text": status.text
        })
        
    except AttributeError:
        pass
    
# Create DataFrame
df = pd.DataFrame(tweets)
cols = ["date", "id", "text"]
df = df[cols]
print(df.head())

# write to file
df.to_csv(f'btc_tweets_{date_since}.csv', index=False, encoding="utf-8")