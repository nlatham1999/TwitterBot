from datetime import time
import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def send_tweet(message):
    api.update_status(message)
    print("sent tweet: ", message)

def delete_old_tweets(timeline):
    i = 0
    for tweet in timeline:

        date = tweet._json['created_at']
        text = tweet._json['text']
        year = int(date.split(" ")[-1])
        print(i, " ", year)
        i += 1
        if year < 2021:
            api.destroy_status(tweet.id)
            print("deleting: ", text)

def delete_fleets(timeline):
    for tweet in timeline:
        text = tweet._json['text']
        if "#fleet" in text:
            api.destroy_status(tweet.id)
            print("deleting: ", text)


user = api.me()
print (user.name)


# delete_old_tweets(timeline)

# while True:
#     timeline = tweepy.Cursor(api.user_timeline).items()
#     delete_fleets(timeline)
#     time.sleep(7200)




