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


# MAPPING TABLE

from prettytable import PrettyTable
for label, data in (('Word', words),
	('Screen Name', screen_names),
	('Hashtag', hashtags)):
	pt = PrettyTable(field_names=[label, 'Count'])
	c = Counter(data)
	[ pt.add_row(kv) for kv in c.most_common()[:10] ]
	pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
	print pt



# LEXICAL DIVESIRY

def lexical_diversity(tokens):
	return 1.0*len(set(tokens))/len(tokens)    #we are using set to remove similar elements



def average_words(statuses):
	total_words = sum([len(s.split()) for s in statuses])
	return 1.0*total_words/len(statuses)

print
print
print "LEXICAL DIVERSITY"
print 
print 


print lexical_diversity(words)
print lexical_diversity(screen_names)
print lexical_diversity(hashtags)
print average_words(status_texts)