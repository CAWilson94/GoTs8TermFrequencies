import tweepy 
import globals as gl

from gotListener import GoTListener
from preprocessor import PreProcessor 


consumer_key = gl.Consumers.consumer_key
consumer_secret = gl.Consumers.consumer_secret
access_token = gl.AccessTokens.access_token
access_token_secret = gl.AccessTokens.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#twitter_stream = tweepy.Stream(auth, GoTListener())
#twitter_stream.filter(track=['#gameofthrones'])

pp = PreProcessor()
pp.process_tweets('output_files/example_file.json')