# Author: Laith Abu-Nawwas
# Co-author: ChatGPT

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="twitter-scraper",
    version="0.1",
    description="Scrape Twitter for tweets based on a specified hashtag or keywords",
    author="LANAWWAS / ChatGPT4 Co-Pilot",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            "twitter-scraper=twitter_scraper.main:main"
        ]
    },
)
