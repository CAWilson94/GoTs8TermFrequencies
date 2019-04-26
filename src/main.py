import tweepy 
from gotListener import GoTListener

consumer_key = 'uKvHiugPJ7zYeDgWRddLDCgVf'
consumer_secret = 'Msx82y6h4MdAkoCXtSSdDUDWorLhebVf8cByA0ASDgN3AShzBX'
access_token = '216437150-YKQh9phgT8L0ot2cm1WhQJJfthnMxhO3xYmlRQ8E'
access_token_secret = 'rhJgB2rQCQ2BOpMJe9PuNhvMOJtD2ECeynzz7HMpIfNfV'

# TODO: pop the keys into some other nice place instead of hard coding. Thanks. 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# TODO: shove a stream listener class in another file keep connections open for term frequencies. 

twitter_stream = tweepy.Stream(auth, GoTListener())
twitter_stream.filter(track=['#gameofthrones'])