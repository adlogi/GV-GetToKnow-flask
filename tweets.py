import tweepy

def country_tweets(country):
    public_tweets = tweepy.api.search(country)
    return [tweet.text for tweet in public_tweets]

