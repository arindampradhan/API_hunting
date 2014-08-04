import os
import httplib2
import json
import apiclient.discovery
from BeautifulSoup import BeautifulStoneSoup
from nltk import clean_html

USER_ID = '107033731246200681024' # Tim O'Reilly

# XXX: Re-enter your API_KEY from  https://code.google.com/apis/console 
# if not currently set
API_KEY = 'AIzaSyDJ6RNSOiPun0-FZHsS_WUeGN0FPiNtHeA' 

MAX_RESULTS = 200 # Will require multiple requests

def cleanHtml(html):
  if html == "": return ""

  return BeautifulStoneSoup(clean_html(html),
          convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]

service = apiclient.discovery.build('plus', 'v1', http=httplib2.Http(), 
                                    developerKey=API_KEY)

activity_feed = service.activities().list(
  userId=USER_ID,
  collection='public',
  maxResults='100' # Max allowed per request
)

activity_results = []

while activity_feed != None and len(activity_results) < MAX_RESULTS:

  activities = activity_feed.execute()

  if 'items' in activities:

    for activity in activities['items']:

      if activity['object']['objectType'] == 'note' and \
         activity['object']['content'] != '':

        activity['title'] = cleanHtml(activity['title'])
        activity['object']['content'] = cleanHtml(activity['object']['content'])
        activity_results += [activity]

  # list_next requires the previous request and response objects
  activity_feed = service.activities().list_next(activity_feed, activities)

# Write the output to a file for convenience

f = open(os.path.join('/home/ragnarock/Dropbox/codebase/github/API_hunting/google+', 'jase', USER_ID + '.json'), 'w')
f.write(json.dumps(activity_results, indent=1))
f.close()

print str(len(activity_results)), "activities written to", f.name
