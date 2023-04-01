# Twitter Scraper

This code is a test of ChatGPT 4 capabilities and some fun around using AI-based Co-pilot for coding.

## Usage

1. Update the `config.yaml` file with your Twitter search terms of interest.
2. Install the package using `python setup.py install`.
3. Run the script using `python twitter_scraper.py`.

## Output

The script will output a CSV file named `tweets.csv` containing the following columns (Can be modified in `config.yaml`):

- `id`: The tweet ID.
- `created_at`: The date the tweet was created.
- `content`: The tweet text.
- `username`: The username of the tweet author.
- `location`: The location of the tweet author.
- `sentiment`: The sentiment polarity -1 to 1 of the tweet (if sentiment analysis is enabled).
- `sentiment_category`: The sentiment classification.
- `likes`
- `retweets`
- `language`

## Sentiment Analysis

The script supports sentiment analysis in both Arabic and English. To enable sentiment analysis, set the `sentiment` parameter in the `config.yaml` file to `True`.

### Sentiment Categories

The sentiment analysis categorizes tweets into the following categories:

- `happy`: Positive sentiment.
- `neutral`: Neutral sentiment.
- `mad`: Negative sentiment.

Note: The sentiment analysis is not perfect and may not always accurately reflect the sentiment of the tweet.

## Disclaimer

This code is a test of ChatGPT 4 capabilities and some fun around using AI-based Co-pilot for coding. Use it at your own risk.```
