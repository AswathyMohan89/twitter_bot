# Dependencies
import tweepy
import json
import time
import random

# Twitter API Keys
access_token  = '1851468854-znPKyGnJiKd72fDF2mSocYgnqJlNYfDtX31RlgD'
access_token_secret  = 'w4OuJGKMtJSdItnFCJ40hTZMUprxlHbs7gboNnbA3f1AW'
consumer_key= 'brfyAZHV4NsabPoeHsE0ZezHp'
consumer_secret= 'OSFRHXUvyr4PaOJdDN4axHRrDGa4iHSYbmCpZLZ1wf4cBH9WvS'

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create a function that tweets
# CODE GOES HERE
# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        random.choice(happy_quotes)+"This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1