import tweepy 
from gotListener import GoTListener
import globals as gl

consumer_key = gl.Consumers.consumer_key
consumer_secret = gl.Consumers.consumer_secret
access_token = gl.AccessTokens.access_token
access_token_secret = gl.AccessTokens.access_token_secret

# TODO: pop the keys into some other nice place instead of hard coding. Thanks. 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# TODO: shove a stream listener class in another file keep connections open for term frequencies. 

twitter_stream = tweepy.Stream(auth, GoTListener())
twitter_stream.filter(track=['#gameofthrones'])