import urllib2
from bs4 import BeautifulSoup
url = "http://www.packtpub.com/books"
page = urllib2.urlopen(url)
soup_packtpage = BeautifulSoup(page)
page.close()

all_books_table = soup_packtpage.find("table",class_="views-view-grid")

all_book_titles = all_books_table.find_all("div",class_="views-field-title")

for book_title in all_book_titles:
	book_title_span = book_title.span
	print("Title Name is :"+book_title_span.a.string)
	published_date = book_title.find_next("div",class_="views-field-field-date-of-publication-value")
	print("Published Date is :"+published_date.span.string)
	price = book_title.find_next("div",class_="views-field-sell-price")
	print("Price is :"+price.span.string)
