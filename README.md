# Twitter Sentiment Analysis

This is a work in progress. You need to have python installed on your machine.


## Project setup

Install Matplotlib, Pandas, Tweepy and TextBlob libraries:
```
pip install tweepy textblob matplotlib pandas
```

In order to access the Twitter Streaming API, you need to register an application at http://apps.twitter.com. Once created, you should be redirected to your app’s page, where you can get the consumer key and consumer secret and create an access token under the “Keys and Access Tokens” tab. Use these in config_example.py and rename the file as config.py.


## Run

Stream the sentiment associated to a word:
```
python sentiment-word.py
```
(Press Ctr + C to end the program)


Get the sentiment associated to a user's last 10 tweets:
```
python sentiment-username.py
```


## Roadmap

Backend:
- Make API endpoints
- Use Textblob to get more data

Fronted:
- Make frontend
