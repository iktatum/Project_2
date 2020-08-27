# Project #2 Final Analysis
  Bitcoin_Sentiment Analysis and Trade Signal Evaluation 

## Group Members: Alex Waters, Joe Swiderski,  Ivan Tatum

* We are looking to attempt to determine if we can predict bitcoin prices using the fear and greed index as a proxy for sentiment analysis. Are we bale to make buy or sell decisions in bitcoing to take advantage of price moves.

* Gathering Data 
  - Obtain bitcin price, S&P , and bitcoin volume as feathure to evaluate. This data was o btain from Google Sheets and Yahoo.
  - We had to use the TWitter API (TWeepy) to download twitter feeds.
  - Score these tweets for positive, negagtive, or neutral sentiment 
  - Use VADER, IBM Watson, FNG to produce scores 

* Getting reliable data was the first item to tackle. We eventually used data from February 2018 to Current because of the availability of free data to pull.  In the data training process, we used the LSTM and SARIMAX models to evaluate how well the models predicted the bitcoin price. ONce the data was trained by these models, using 70% of the data and testing the data with the remining 30%, we could get evaluate the predictive ability of the model.  

* The SARIMAX model is a regression model used to evaluate seasonality and to make predictions if seasonality did exit. Many investments have seasonal components and therefore, we used this model to rule out the possibility of seaosnality.

* Both the LSTM and teh SARIMAX models had poor rsults when itcomes to predictive power. There is simply not enough relvant data to use to be able to extract features relevant to predicting price. There is a lot of extraneous data that has no effect on bitcoin price action. We do believe the passage of time and the adoption of cryptocurrency as a norm will allow the model to eveolve so that tey will eventuall yhave more predictve power.

* 

* [ ] Discuss the implications of your findings. This is where you get to have an open-ended discussion about what your findings mean.
