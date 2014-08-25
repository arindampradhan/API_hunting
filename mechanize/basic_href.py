import urllib2
from bs4 import BeautifulSoup

url = "http://arindam2u.com"
page = urllib2.urlopen(url)


soup  = BeautifulSoup(page)

for tag in soup.findAll('a',href=True):
	print tag['href']




##using mechanize

"getting href is easier with mechanize"

##url = "http://arindam2u.com"

br = mechanize.Browser()
##mechanize is like a browser

br.open(url) 

for link in br.links():
	print link



##or print both base url and link url

for link in br.links():
	print "the base url is: " + link.base_url
	print "the url is: " + link.url





##print 

for link in br.links():
	newurl = urlparse.urljoin(link.base_url,link.url)
	print newurl



##print path only

for link in br.links():
	newurl = urlparse.urljoin(link.base_url,link.url)	
	b1 = urlparse.urlparse(newurl).hostname
	b2 = urlparse.urlparse(newurl).path
	print "http://" +b1+b2
	
