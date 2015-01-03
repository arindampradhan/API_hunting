import twitter
CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# print twitter_api
# import tweet
# WORLD_WOE_ID = 1
# US_WOE_ID = 23424977


# # world trends

# world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
# us_trends = twitter_api.trends.place(_id=US_WOE_ID)




import json
# print world_trends
# print
# print us_trends

# print json.dumps(world_trends, indent=1)
# print 
# print json.dumps(us_trends, indent=1)


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
# # Explore the first 5 items for each...
# print
# print
# print

# print json.dumps(status_texts[0:5], indent=1)
# print json.dumps(screen_names[0:5], indent=1)
# print json.dumps(hashtags[0:5], indent=1)
# print json.dumps(words[0:5], indent=1)

from collections import Counter

# for item in [words,screen_names,hashtags]:
# 	c = Counter(item)
# 	print c.most_common()[:10]
# 	print 

from prettytable import PrettyTable
# for label, data in (('Word', words),
# 	('Screen Name', screen_names),
# 	('Hashtag', hashtags)):
# 	pt = PrettyTable(field_names=[label, 'Count'])
# 	c = Counter(data)
# 	[ pt.add_row(kv) for kv in c.most_common()[:10] ]
# 	pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
# 	print pt



# def lexical_driversity(tokens):
# 	return 1.0*len(set(tokens))/len(tokens)

# def average_words(statuses):
# 	total_words= sum([len(s.split() for s  in statuses ])
# 	return 1.0*total_words/len(statuses)

# print lexical_driversity(words)
# print lexical_driversity(screen_names)
# print lexical_driversity(hashtags)
# print lexical_driversity(status_texts)




retweets = [
	(status['retweet_count'],
	status['retweeted_status']['user']['screen_name'],
	status['text'])

	for status in statuses
	if status.has_key('retweeted_status')
]

pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[ pt.add_row(row) for row in sorted(retweets, reverse=True)[:5] ]
pt.max_width['Text'] = 50
pt.align= 'l'
print pt


import matplotlib.pyplot as plt
word_counts =  sorted(Counter(words).values(),reverse = True)

plt.loglog(word_counts)
plt.ylabel("Freq")
plt.xlabel("Word Rank")
