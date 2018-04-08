from twitter import Twitter, OAuth
import os

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_SECRET']

#print(consumer_key)


t = Twitter(auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))
#t = Twitter(auth=OAuth('22378452-EnmlHrzpURC91d36Huslll575Ayn8Cqse6jTHn4Sn', 'IilDkC8qJUA8a6tiocZPJL4MIQHiXxHnX6cg3XpcUOjwk', 'H9dBp4KxXXXhhL5kzn0yYXvqO', 'imKqXnxkoiEnRRsi7WNwgKxbl5tKt23la7syePpQ6frp4mREYP'))
pythonTweets = t.search.tweets(q="#python")
print(pythonTweets)