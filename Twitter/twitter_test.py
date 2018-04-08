from twitter import Twitter, OAuth
import os
from pprint import pprint

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_SECRET']


t = Twitter(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))
print(dir(t))
#pythonTweets = t.search.tweets(q="#python")
#pprint(pythonTweets)