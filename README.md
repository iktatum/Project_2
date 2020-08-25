d# Project_2 (Day 3) 

Bitcoin_Sentiment Analysis and Trade Signal Evaluation 
-  Adjustments 

## Alex Waters, Joe Swiderski,  Ivan Tatum

- Exploring the Sentiment Analysis to Explain the Predictive Power of Bitcoin and to see if the trading signals can be used to make investment decisions. 


## We made the following changes to our project.

- We had to use a different proxy for sentiment for Fear and Greed (aka FNG) as a proxy for twitter sentiment.
- Data available from 02/01/2018 to Current. Price data went back to 2015, but we had to truncate the the data to reflect the overlap
- We will Correlate the Fear and Greed Index with BTC closing price.
- Twitter sentiment will be modeled using available data (7 days)
- VADER, TextBlob, IBM Watson Sentiment Analyzers
- (NEw) Tweepy – download day’s worth of tweets     
