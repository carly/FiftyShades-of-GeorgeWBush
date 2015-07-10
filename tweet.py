import os 
import twitter



api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

print api.VerifyCredentials()

status = api.PostUpdate("I think when the history of this period of time is written, it will say I'm going to fuck you.")
print status.text