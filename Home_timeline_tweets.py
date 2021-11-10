import tweepy

#Set up Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Download and print out Twitters from the author's home timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#Create a new txt file to store the results
f = open (r'Home_timeline_tweets_results.txt','w')
print (public_tweets,file = f)
f.close()
