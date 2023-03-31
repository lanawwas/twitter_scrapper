#ChatGPT4 as a co-pilot to optimize the code

import tweepy
import yaml
import pandas as pd
from textblob import TextBlob
from langdetect import detect


# Load credentials from YAML config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])

# Initialize API client
api = tweepy.API(auth)

# Define function to perform sentiment analysis
def get_sentiment(text):
    try:
        language = detect(text)
        if language == 'ar':
            blob = TextBlob(text)
        else:
            blob = TextBlob(text, analyzer=TextBlobDE())
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            return 'happy'
        elif sentiment == 0:
            return 'neutral'
        else:
            return 'mad'
    except:
        return 'unknown'

# Define function to scrape tweets
def scrape_tweets(hashtag, lang, country):
    # Define dataframe to store results
    df = pd.DataFrame(columns=["Text", "Language", "Sentiment"])

    # Define query parameters
    query = hashtag + " -filter:retweets"
    if lang != "all":
        query += " lang:" + lang
    if country:
        query += " place_country:" + country

    # Scrape tweets
    for tweet in tweepy.Cursor(api.search_tweets, q=query, tweet_mode="extended").items(config["max_tweets"]):
        text = tweet.full_text
        language = detect(text)
        if lang == "all" or language == lang:
            sentiment = get_sentiment(text)
            df = df.append({"Text": text, "Language": language, "Sentiment": sentiment}, ignore_index=True)

    # Export dataframe to CSV
    df.to_csv(hashtag + ".csv", index=False)

# Load query parameters from YAML config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Scrape tweets for each query in config file
for query in config["queries"]:
    hashtag = query["hashtag"]
    lang = query["language"]
    country = query.get("country")
    scrape_tweets(hashtag, lang, country)
