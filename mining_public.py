# this is for mining public data

import tweepy
import requests
from utils.config import *
client = tweepy.Client(bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

auth_handler = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

# user can input 
user_input = input("Enter an account to search: ")

key_word = user_input
tweet_amount = 10

query = 'ama #ama -web3 lang:en'

# get max. 100 tweets
tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id', 'created_at'],
                                     max_results=10)

import pandas as pd

tweets_dict = tweets.json() 
tweets_data = tweets_dict['data'] 
final_list = []
# analyze tweets content, get the time info, etc.
for tweet in tweets_data:
    # convert to str
    tw = str(tweet['text'])
    if 'Nov' in tw:
        final_list.append(tweet)

df = pd.DataFrame(final_list)

print(df)

# save to csv
df.to_csv('tweets.csv', index=False)
