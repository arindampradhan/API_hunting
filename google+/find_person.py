import httplib2
import json
import apiclient.discovery #
Q = "Tim O'Reilly"
API_KEY = 'AIzaSyDJ6RNSOiPun0-FZHsS_WUeGN0FPiNtHeA'
service = apiclient.discovery.build('plus', 'v1', http=httplib2.Http(),
developerKey=API_KEY)
people_feed = service.people().search(query=Q).execute()
# print json.dumps(people_feed['items'], indent=1)

# for p in people_feed['items']:
# 	print p['image']['url']


import os
import httplib2
import json
import apiclient.discovery
from BeautifulSoup import BeautifulStoneSoup
from nltk import clean_html
USER_ID = '107033731246200681024' # Tim O'Reilly

max_results = 200
def cleanhtml(html):L
	fi html == "":return ""
	return BeautifulSoup(clean_html(html),convertEntities=BeautifulSoup.HTML_ENTITIES).contents[0]

activity_feed = service.activities().list(
	userId =USER_ID
	collection="public"
	maxResults='100'
	)


activity_results = []

while activity_feed != None and len(activity_results) < MAX_RESULTS:
	activities = activity_feed.execute()
	if 'items' in activities:
		for activity in activities['items']:
			if activity['object']['objectType'] == 'note' and \
				activity['object']['content'] != '':

				activity['title'] = cleanHtml(activity['title'])
				activity['object']['content'] = cleanhtml(activity['object']]['content'])
				activity_results += [activity]

		activity_feed = service.activities().list_new(activity_feed,activities)

f = open(os.path.join('resources', 'ch04-googleplus', USER_ID + '.json'), 'w')
f.write(json.dumps(activity_results, indent=1))
f.close()
print str(len(activity_results)), "activities written to", f.name