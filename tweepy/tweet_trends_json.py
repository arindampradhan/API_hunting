import json
import twitter

C_KEY = ''
C_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_SECRET = ''

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
