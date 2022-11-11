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

def user_tweets(user, tweet_amount):

    # user can input 
    user_input = user
    tweet_amount = tweet_amount

    # convert account name to user id
    user_id = client.get_user(username=user_input).json()['data']['id']

    # --- get recent tweets ----
    tweets = client.get_users_tweets(id=user_id, max_results=10, \
                                start_time='2022-11-01T00:00:00Z', \
                                end_time='2022-11-10T00:00:00Z', \
                                tweet_fields=['author_id', 'created_at'])
    # put the tweets into a list
    tweets_list = tweets.json()

    collections = tweets_list['data']
    all_tweets = []
    for item in collections:
        text = item['text']
        created_at = item['created_at'].split('T')[0] + ' ' + item['created_at'].split('T')[1].split('.000Z')[0]
        url = "https://twitter.com/" + item['author_id'] + "/status/" + item['id']
        all_tweets.append([text, created_at, url])
    return all_tweets, collections


def key_word_tweets(key_word, collections):
    # fliter the tweets by 'keyword'
    key_list = []
    print()
    for tweet in collections:
        # check if the tweet contains the keyword
        if key_word in tweet['text']:
            text = tweet['text']
            time = tweet['created_at'].split('T')[0] + ' ' + tweet['created_at'].split('T')[1].split('.000Z')[0]
            url = "https://twitter.com/" + tweet['author_id'] + "/status/" + tweet['id']
            key_list.append([text, time, url])
    return key_list

def format_tweets(collections):
    key_list = collections
    import pandas as pd
    key_list = pd.DataFrame(key_list)
    # rename the columns
    key_list.columns = ['text', 'time', 'url']
    return key_list
def save_to_csv(key_list, file_name):
    # save to csv
    # save to outside output folder

    import os
    if not os.path.exists('output'):
        os.mkdir('output')
    # save to csv
    key_list.to_csv(os.path.join('output', file_name + '.csv'), index=False)
