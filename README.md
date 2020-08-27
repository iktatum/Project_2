# Project #2 Final Results 
  Bitcoin_Sentiment Analysis and Trade Signal Evaluation 

## Group Members: Alex Waters, Joe Swiderski,  Ivan Tatum

* We are looking to attempt to determine if we can predict bitcoin prices using the fear and greed index as a proxy for sentiment analysis. Are we bale to make buy or sell decisions in bitcoing to take advantage of price moves.

* Gathering Data 
  - Obtain bitcin price, S&P , and bitcoin volume as feathure to evaluate. This data was o btain from Google Sheets and Yahoo.
  - We had to use the TWitter API (TWeepy) to download twitter feeds.
  - Score these tweets for positive, negagtive, or neutral sentiment 
  - Use VADER, IBM Watson, FNG to produce scores 

* [ ] Describe the data preparation and model training process. In the data traing and process, we used the LSTM and SARIMAX models to evaluate how well the models predicted the bitcoin price. ONce the data was trained by these models, using 70% of the data and testing the data with the remining 30%, we could get evaluate the predictive ability of the model.  

* The SARIMAX model is a regression model used to evaluate seasonality. Many investments have seasonal components and therefore, we used this model to rule out the possibility of seaosnality.

* [ ] Summarize your conclusions and predictions. This should include a numerical summary (what data your model yielded), as well as visualizations of that summary (plots of the final model evaluation and predictions).

* [ ] Discuss the implications of your findings. This is where you get to have an open-ended discussion about what your findings mean.
