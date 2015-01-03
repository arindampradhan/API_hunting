import twitter
CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api
import tweet
WORLD_WOE_ID = 1
US_WOE_ID = 23424977


# world trends

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)




import json
print world_trends
print
print us_trends

print json.dumps(world_trends, indent=1)
print 
print json.dumps(us_trends, indent=1)

