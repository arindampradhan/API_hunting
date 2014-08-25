import mechanize
import re

br = mechanize.Browser()
br.addheaders = [('User-agent','Mozilla/5.0')]

br.set_handle_robots(False)

html = br.open('http://www.google.com/search?q=python')

html = html.read().lower()

#handling unicode

html = unicode(html,errors='ignore')

print html



## lets get them with a patter

pattern = re.compile(r'<span class="\*st\*">(.*?)</span>',re.MULTILINE)

match_description = re.findall(pattern,html)

print match_description
