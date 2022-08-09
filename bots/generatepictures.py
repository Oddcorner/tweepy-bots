#!/usr/bin/env python
# tweepy-bots/bots/generatepictures.py
from requests import get
import logging
from config import create_api
import time
from imageAPI import generate_picture
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

username = 'oddcorner'
latest_tweet_id_str = 'defaultString'

def get_latest_tweet(api):
    global latest_tweet_id_str
    tweets_list = []
    logger.info("Retrieving lastest tweet from " + username)
    try:
        tweets_list = api.user_timeline(screen_name=username, count=1, include_rts=False, exclude_replies=True)
    except Exception as e:
        logger.error("Error fetching user tweets", exc_info=True)
        raise e

    # Return if latest tweet is a RT or reply
    if len(tweets_list) == 0:
        return None
    
    tweet = tweets_list[0]

    # Returns if latest tweet has already been processed.
    if tweet.id_str == latest_tweet_id_str:
        return None

    return tweet

def update_latest_tweet_id_str(api):
    global latest_tweet_id_str
    tweets_list = []
    logger.info("Updating lastest tweet from " + username)
    try:
        tweets_list = api.user_timeline(screen_name=username, count=1, include_rts=False, exclude_replies=True)
    except Exception as e:
        logger.error("Error fetching user tweets", exc_info=True)
        raise e

    # Return if no tweets on account 
    if len(tweets_list) == 0:
        return

    latest_tweet_id_str = tweets_list[0].id_str

def remove_hyperlinks(text):
    return text.split("https://")[0]

def generate_pic(tweet):
    global latest_tweet_id_str
    if tweet == None:
        return None
    
    text = remove_hyperlinks(tweet.text)
    id_str = tweet.id_str

    # Returns None if tweet is just a link i.e no text.
    if len(text) == 0:
        return None
    
    # Actual code.
    pic_url = generate_picture(text)

    if pic_url == None:
        return None
    
    # Updates global latest tweet variable
    latest_tweet_id_str = id_str

    returnObj = [pic_url, text]
    return returnObj

def post_picture(api, pic):
    if pic == None:
        return
    url = pic[0]
    text = pic[1]

    filename = 'temp.jpg'
    request = get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        media = api.media_upload(filename)
        api.update_status(status=text,media_ids=[media.media_id_string])
        os.remove(filename)
        logger.info("Tweet posted!")
    else:
        logger.error("Unable to post tweet")

def main():
    api = create_api()
    update_latest_tweet_id_str(api)
    while True:
        tweet = get_latest_tweet(api)
        pic = generate_pic(tweet)
        post_picture(api, pic)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
