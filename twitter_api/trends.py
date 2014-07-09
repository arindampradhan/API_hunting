import twitter
CONSUMER_KEY = 'iyijz0WauC47JhldDofD5Sxrq'
CONSUMER_SECRET ='FoHv0HGkYYrSgWcXEEdIXWyw8L3zCbQqXR69w2tZhLaW8qah52'
OAUTH_TOKEN = '2193588674-W5Zq9smc5F4RRVHI23E7AVFpgdLf9WcZQIKSJmA'
OAUTH_TOKEN_SECRET = 'Pr3CMTlToMrmPvnsReG5M06zDdtNtmiE8MaskOQpDhT34'

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

