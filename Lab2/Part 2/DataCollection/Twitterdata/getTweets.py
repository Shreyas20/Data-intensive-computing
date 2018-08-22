import tweepy
import csv
import pandas as pd

consumer_key = 'XvVQsNpTZSLorkcht0ndsO3Wb'
consumer_secret = 'hFcXEdk3lyi8s0sP6xeAv5ns1wtUDTbH3fSBubcWH38eQZKGTf'
access_token = '1536168896-xgL8sNgNuSUroWywj2Ev34REuFbS9oPyjmULYNh'
access_token_secret = 'o67cgzE9Ly3ehxh3T0elMgXYkOg2VeyNQMs8ftteQ9Kjw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('tweetsday.txt', 'a')
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,q="shooting",
                           tweet_mode='extended',lang="en",
                           since="2018-04-07").items():
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):

        #print (tweet.full_text)
        csvWriter.writerow([tweet.full_text.encode('utf-8')])

csvFile.close()
