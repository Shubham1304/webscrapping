import urllib.request as urllib2
from bs4 import BeautifulSoup

import webbrowser

new=2

tabUrl="http://google.com/?#q="

term=input("Enter search query")

#webbrowser.open(tabUrl+term,new=new)

quote_page=(tabUrl+term)

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find("div", attrs={ "class" : "rc" })
print (name_box)
