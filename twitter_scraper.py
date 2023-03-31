#ChatGPT4 as a co-pilot to optimize the code

import tweepy
import yaml
from searchtweets import ResultStream, gen_request_parameters, load_credentials

# Load Twitter API credentials from YAML file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
# auth.set_access_token(config['access_token'], config['access_secret'])

# Create API object
api = tweepy.API(auth)

# Define the search query
query = config['search_query']
language = config['language']
if 'country' in config:
    query += f' lang:{language} place_country:{config["country"]}'
else:
    query += f' lang:{language}'

# Scrape tweets
# tweets = tweepy.Cursor(api.search_tweets, q=query, tweet_mode='extended', lang=language).items() // only in extended access API not in basic API v2 endpoint 

# tweets =  gen_request_parameters(query=query, results_per_call=10)

rule = gen_request_parameters(query=query, tweet_fields=["created_at", "public_metrics", "author_id", "lang", "conversation_id", "in_reply_to_user_id", "referenced_tweets"], expansions=["author_id"], user_fields=["username", "public_metrics", "verified"], place_fields=["full_name", "country_code"], media_fields=["duration_ms", "height", "media_key", "public_metrics", "type", "width", "url"], max_pages=1, tweet_mode='extended')
tweets = ResultStream(rule_payload=rule,
                      max_results=10,
                      tweet_mode='extended').stream()

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
