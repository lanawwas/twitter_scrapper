#ChatGPT4 as a co-pilot to optimize the code

#ChatGPT4 as a co-pilot to optimize the code

import yaml
import snscrape.modules.twitter as sntwitter
import pandas as pd
from langdetect import detect
from textblob import TextBlob


# Load Twitter API credentials from YAML file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Define the search query
query = config['search_query']
if 'hashtag' in config:
    query += ' ' + config['hashtag']
if 'from' in config:
    query += ' from:' + config['from']
if 'since' in config:
    query += ' since:' + config['since']
if 'until' in config:
    query += ' until:' + config['until']
if 'country' in config:
    query += f' lang:{config["language"]} near:"{config["country"]}" within:{config["radius"]}'
else:
    query += f' lang:{config["language"]}'

# Fetch tweets using snscrape
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= config['max_tweets']:
        break
    tweet_dict = {}
    tweet_dict['date'] = tweet.date.strftime('%Y-%m-%d %H:%M:%S')
    tweet_dict['id'] = tweet.id
    tweet_dict['content'] = tweet.content
    tweet_dict['username'] = tweet.user.username
    tweet_dict['hashtags'] = ', '.join([hashtag.text for hashtag in tweet.hashtags])
    tweet_dict['retweets'] = tweet.retweetCount
    tweet_dict['likes'] = tweet.likeCount
    tweet_dict['language'] = detect(tweet.content)
    tweets.append(tweet_dict)

# Sentiment analysis
if 'sentiment' in config and config['sentiment']:
    for tweet in tweets:
        if tweet['language'] == 'ar':
            blob = TextBlob(tweet['content'])
            tweet['sentiment'] = blob.sentiment.polarity
        else:
            blob = TextBlob(tweet['content'])
            tweet['sentiment'] = blob.sentiment.classification
            
# Check if all required columns are present in the data
df = pd.DataFrame(tweets)
print(df.columns)

            
# Save tweets to CSV file
#df = pd.DataFrame(tweets)

#if 'attributes' in config:
#    df = df[config['attributes']]
#df.to_csv(config['output_file'], index=False, encoding='utf-8-sig')

#print(f'{len(tweets)} tweets were scraped and saved to {config["output_file"]}')
