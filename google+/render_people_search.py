from find_person import *

from IPython.core.display import HTML

html=[]

for p in people_feed['items']:
	html+="<img src="%s">"%(p['image']['url'])
	

HTML(''.join(html))

