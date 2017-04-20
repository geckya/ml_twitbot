import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#print(api + '\n')

# For loop to iterate over tweets with #machinelearningflashcards, limit to 10
for tweet in tweepy.Cursor(api.search,q='#machinelearningflashcards').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)
        # Retweet tweets as they are found
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
           tweet.retweet()
           print('Retweeted the tweet')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

