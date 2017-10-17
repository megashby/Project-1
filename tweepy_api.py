

import sys
#csv is the output we'll write to
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
#These are keys that twitter gives you when you register an App
#for simplicity, we'll leave them here but for security's sake
#we should have it read the keys off of a seperate file, so we can turn the project in
#without giving other people access to our keys.
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"

#here is an example of gathering 100 tweets using tweepy
def get_tweets(username):

    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    #this block of code authenticates us with twitter's db
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #set count to however many tweets you want; twitter only allows 200 at once
    number_of_tweets = 100

    #takes username and number of tweets and gets tweets
    tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

    #create array of tweet information: username, tweet id, date/time, text
    tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

    #write to a new csv file from the array of tweets
    print "writing to {0}_tweets.csv".format(username)
    with open("{0}_tweets.csv".format(username) , 'w+') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(tweets_for_csv)

#this code doesn't run because it's just an example. 
#We'll have to integrate it into our project.
#All this info was gathered from tutorials.
#tweepy makes it super easy.