# Twitter Sentiment Analysis

This is a work in progress. You need to have python installed on your machine.


## Project setup

Install Tweepy and TextBlob libraries:
```
pip install tweepy textblob
```

In order to access the Twitter Streaming API, you need to register an application at http://apps.twitter.com. Once created, you should be redirected to your app’s page, where you can get the consumer key and consumer secret and create an access token under the “Keys and Access Tokens” tab. Use these in config_example.py and rename the file as config.py.


## Run

```
python sentiment.py
```

Press Ctr + C to end the program


## Roadmap

Backend:
- Make API endpoints
- Use Textblob to get more data

Fronted:
- Make frontend
