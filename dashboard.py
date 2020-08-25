"""
Near realtime dashboard to track BTC price and Twitter sentiment
"""

import pandas as pd
from datetime import datetime as dt
import tweesmu as tw
import pandas_datareader.data as web 
import dash 
import dash_core_components as dcc     
import dash_html_components as html
from yahoo_fin import stock_info as si
from dash.dependencies import Input, Output 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

# remove zombie pickle files if they exist. Ignore if it does not
try:
    os.remove("./sensitivity.pkl")
except Exception as e:
    pass

try:
    os.remove("./price.pkl")
except Exception as e:
    pass

def processSentiment(tweets):
    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    s = []

    for tweet in tweets:
        try:
            text = tw.processTweet(tweet['text'])
            date = pd.to_datetime(tweet['date'], infer_datetime_format=True)
            id = tweet['id']
            sentiment = analyzer.polarity_scores(text)
            if sentiment["compound"] == 0.0: continue

            s.append({
                "id": id,
                "date": date,
                "text": text,
                "compound": sentiment["compound"],
                "positive": sentiment["pos"],
                "negative": sentiment["neg"],
                "neutral": sentiment["neu"]
            })
            
        except Exception as e:
            pass
        
    # Create DataFrame
    df = pd.DataFrame(s)
    df.set_index("id", inplace = True)
    return df

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Stock Visualisation"

app.layout = html.Div([
    dcc.Interval(id='interval1', interval=301*1000), # add 1 seconds to avoid the rate limit
    html.H6("Stock Visualisation Dashboard"),
    html.Br(),
    html.Div(id='sentiment'),
    html.Br(),
    html.Div(id ='price')
])


@app.callback(
    Output(component_id='sentiment', component_property='children'),
    [dash.dependencies.Input('interval1', 'n_intervals')])

def update_interval(n):
    stock='BTC-USD'
    df = None
    # restore session data. if it does not exist, create new dataframe
    try:
        df = pd.read_pickle("./sensitivity.pkl")
    except Exception as e:
        df = pd.DataFrame(columns=["Date", "BTC_Sentiment"])


    tweets = tw.getTweets('Bitcoin', 300) # rate limit of 900 per every 15 minutes
    df_sentiment = processSentiment(tweets)
    new_row = {'Date':df_sentiment['date'][0], 'BTC_Sentiment':df_sentiment['compound'].mean()}
    #append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    # write session data
    df.to_pickle("./sensitivity.pkl")

    return dcc.Graph(id ="example", 
        figure ={ 
            'data':[{'x':df.Date, 'y':df.BTC_Sentiment, 'type':'line', 'name':'Bitcoin Sentiment'}, 
            ], 
            'layout':{ 
                'title':'Bitcoin Sentiment. 1 = Greed. -1 = Fear.' 
            } 
        } 
    ) 

@app.callback(
    Output(component_id='price', component_property='children'),
    [dash.dependencies.Input('interval1', 'n_intervals')])
    
def update_interval(n):
    stock='BTC-USD'
    df = None
    # restore session data. if it does not exist, create new dataframe
    try:
        df = pd.read_pickle("./price.pkl")
    except Exception as e:
        df = pd.DataFrame(columns=["Date", "BTC_Price"])

    # get live price of Bitcoin
    price = si.get_live_price("BTC-USD")
    new_row = {'Date':dt.utcnow(), 'BTC_Price':price}
    #append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    # write the session data
    df.to_pickle("./price.pkl")

    return dcc.Graph(id ="example", 
        figure ={ 
            'data':[{'x':df.Date, 'y':df.BTC_Price, 'type':'line', 'name':'BTC-USD Price'}, 
            ], 
            'layout':{ 
                'title':'BTC-USD Price' 
            } 
        } 
    ) 


if __name__ == '__main__':
    app.run_server(debug=True)

