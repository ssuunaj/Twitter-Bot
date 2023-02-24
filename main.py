import gspread

import tweepy

from tokens import consumer_secret,consumer_key,access_token,access_token_secret


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("Tweets").sheet1

#get next tweet
next_tweet = wks.acell('A2').value

#post tweet through twitter api
client.create_tweet(
    text=next_tweet
)

#delete row on success
wks.delete_rows(2)