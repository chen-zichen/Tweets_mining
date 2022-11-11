# this is for mining user data

import tweepy
import requests
from utils.config import *
from utils.get_tweets import *

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



if __name__ == '__main__':
    user_id = input("Enter an account to search: ")
    tweet_amount = input("Enter the amount of tweets to search: ")
    key_word = input("Enter the keyword to search: ")
    all_tweets, collections = user_tweets(user_id, tweet_amount)
    all_tweets = format_tweets(all_tweets)
    save_to_csv(all_tweets, 'all_tweets')

    # from the collections to get the tweets with the keyword
    key_list = key_word_tweets(key_word, collections)   
    key_list = format_tweets(key_list)
    save_to_csv(key_list, 'key_tweets')