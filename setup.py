from setuptools import setup

setup(
    name="twitter-scraper",
    version="0.1",
    description="Scrape Twitter for tweets based on a specified hashtag or keywords",
    author="LANAWWAS / ChatGPT4 Co-Pilot",
    packages=["twitter_scraper"],
    install_requires=[
        "tweepy",
        "pyyaml",
        "textblob",
        "langdetect"
    ],
    entry_points={
        "console_scripts": [
            "twitter-scraper=twitter_scraper.main:main"
        ]
    }
)
