# Tweet2Img Twitter bot

A simple twitter bot that listens for new tweets from [@oddcorner](https://twitter.com/Oddcorner) and automatically creates and posts AI generated images on [@bot_corner](https://twitter.com/Bot_corner) using the tweet's text as a prompt.

## Technologies

This project is created with:

- Python 3.8
- [Tweepy 4.1](https://github.com/tweepy/tweepy.git)
- [DeepAI text2img API](https://deepai.org/machine-learning-model/text2img)

## Setup

To run this project, you will need to provide your own .env file in /bots/.env containing:

```
CONSUMER_KEY={YOUR_TWITTER_CONSUMER_KEY}
CONSUMER_SECRET={YOUR_TWITTER_CONSUMER_SECRET}
ACCESS_TOKEN={YOUR_TWITTER_ACCESS_TOKEN}
ACCESS_TOKEN_SECRET={YOUR_TWITTER_ACCESS_TOKEN_SECRET}
AI_KEY={YOUR_DEEPAI_API_KEY}
```

Then simply run `python generatepictures.py` to start the bot.

## Future Improvements

- Utilise threading to handle higher volumes of tweets at a time
- Use Monads instead of passing and checking for "None"

## Acknowledgments

This project was adapted from the guide [How to make a twitter bot in Python](https://realpython.com/twitter-bot-python-tweepy/).
