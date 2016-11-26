from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def findQuote(data):
	quote = data.find('span',attrs={'class':'bqQuoteLink'}).text
	author = data.find('div',attrs={'class':'bq-aut'}).find('a').text
	return quote,author

url="https://www.brainyquote.com/quotes/topics/topic_age.html"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req)
#print(type(page))
#print(page)
soupData = BeautifulSoup(page,"html.parser")
#print(soupData.prettify())
#chcp 65001
#windows ke cmd ki default encoding doosri hoti h
#print(soupData)
#print(type(soupData))
for data in soupData.findAll('div',attrs={'class' : 'masonryitem'}):
	#print(data)
	quote,author = findQuote(data)
	print(quote)
	print(author)
	print("-----------------------------------------")