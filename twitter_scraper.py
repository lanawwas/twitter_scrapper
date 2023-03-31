#ChatGPT4 as a co-pilot to optimize the code

import tweepy
import yaml

# Load Twitter API credentials from YAML file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    config['consumer_key'], config['consumer_secret'],
    config['access_token'], config['access_token_secret']
)
api = tweepy.API(auth)

# Define the search query
query = config['search_query']
language = config['language']
if 'country' in config:
    query += f' lang:{language} place_country:{config["country"]}'
else:
    query += f' lang:{language}'

# Scrape tweets
tweets = tweepy.Cursor(api.search_tweets, q=query, tweet_mode='extended', lang=language).items()

# Sentiment analysis
if 'sentiment' in config and config['sentiment']:
    from langdetect import detect
    from textblob import TextBlob

    for tweet in tweets:
        if tweet.full_text.startswith('RT'):
            continue
        if detect(tweet.full_text) == 'ar':
            blob = TextBlob(tweet.full_text)
            sentiment = blob.sentiment.polarity
        else:
            blob = TextBlob(tweet.full_text, analyzer=NaiveBayesAnalyzer())
            sentiment = blob.sentiment.classification
        print(f'Tweet: {tweet.full_text}')
        print(f'Sentiment: {sentiment}\n')
else:
    # Save tweets to CSV file
    with open('tweets.csv', 'w', encoding='utf-8') as f:
        for tweet in tweets:
            if tweet.full_text.startswith('RT'):
                continue
            f.write(f'{tweet.created_at},{tweet.full_text.replace(",", "")},{tweet.user.screen_name}\n')
