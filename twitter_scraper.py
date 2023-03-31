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

tweets =  gen_request_parameters(query=query, results_per_call=10)
# Save tweets to CSV file
with open('tweets.csv', 'w', encoding='utf-8') as f:
 for tweet in tweets:
  f.write(f'{tweet})
