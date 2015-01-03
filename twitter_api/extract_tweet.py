import twitter
CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

import json

q = "#coding"

count = 100

search_results = twitter_api.search.tweets(q=q,count=count)
statuses = search_results['statuses']




for _ in range(5):
	print "Length of statuses", len(statuses)
	try:
		next_results = search_results['search_metadata']['next_results']
	except KeyError, e: # No more results when next_results doesn't exist
		break
	# Create a dictionary from next_results, which has the following form:
	# ?max_id=313519052523986943&q=NCAA&include_entities=1
	kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
	search_results = twitter_api.search.tweets(**kwargs)
	statuses += search_results['statuses']


status_texts = [ status['text']
for status in statuses ]
screen_names = [ user_mention['screen_name']
for status in statuses
for user_mention in status['entities']['user_mentions'] ]
hashtags = [ hashtag['text']
for status in statuses
for hashtag in status['entities']['hashtags'] ]
# Compute a collection of all words from all tweets
words = [ w
for t in status_texts
for w in t.split() ]


print
print
print

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)
