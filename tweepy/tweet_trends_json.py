import json
import twitter

C_KEY = 'iyijz0WauC47JhldDofD5Sxrq'
C_SECRET = 'FoHv0HGkYYrSgWcXEEdIXWyw8L3zCbQqXR69w2tZhLaW8qah52'
OAUTH_TOKEN = '2193588674-W5Zq9smc5F4RRVHI23E7AVFpgdLf9WcZQIKSJmA'
OAUTH_SECRET = 'Pr3CMTlToMrmPvnsReG5M06zDdtNtmiE8MaskOQpDhT34'

auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_SECRET,C_KEY,C_SECRET)

twitter_api = twitter.Twitter(auth=auth)


# print twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
world_trends  = twitter_api.trends.place(_id = WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id = US_WOE_ID)


# Example 1-7. Creating a basic frequency distribution from the words in tweets
from collections import Counter
for item in [words, screen_names, hashtags]:
c = Counter(item)
print c.most_common()[:10] # top 10
print

print json.dumps(world_trends,indent = 1)
print 
print json.dumps(us_trends,indent = 4)
