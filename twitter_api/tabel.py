import twitter
CONSUMER_KEY = 'iyijz0WauC47JhldDofD5Sxrq'
CONSUMER_SECRET ='FoHv0HGkYYrSgWcXEEdIXWyw8L3zCbQqXR69w2tZhLaW8qah52'
OAUTH_TOKEN = '2193588674-W5Zq9smc5F4RRVHI23E7AVFpgdLf9WcZQIKSJmA'
OAUTH_TOKEN_SECRET = 'Pr3CMTlToMrmPvnsReG5M06zDdtNtmiE8MaskOQpDhT34'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)




import json

q = "#coding"

count = 100

search_results = twitter_api.search.tweets(q=q,count=count)
statuses = search_results['statuses']

for _ in range(5):
	print "length of statuses",len(statuses)
	try:
		next_result = search_results['search_metadata']['next_result']
	except KeyError,e:
		break
	kwargs = dict([kv.split('=') for kn in next_result[1:].split("&")])	

	search_results = twitter_api.search.tweets(**kwargs)
	statuses += search_results['statuses']

# print json.dumps(statuses[0],indent=1)

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

from collections import Counter

for item in [words,screen_names,hashtags]:
	c = Counter(item)
	print c.most_common()[:10]
	print 

from prettytable import PrettyTable
for label, data in (('Word', words),
	('Screen Name', screen_names),
	('Hashtag', hashtags)):
	pt = PrettyTable(field_names=[label, 'Count'])
	c = Counter(data)
	[ pt.add_row(kv) for kv in c.most_common()[:10] ]
	pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
	print pt