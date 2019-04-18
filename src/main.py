import tweepy 

consumer_key = 'key here'
consumer_secret = 'key here'
access_token = 'key here'
access_token_secret = 'key here'

# TODO: pop the keys into some other nice place instead of hard coding. Thanks. 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# TODO: shove a stream listener class in another file keep connections open for term frequencies. 