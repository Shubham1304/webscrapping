import urllib.request as urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import webbrowser

new=2

tabUrl="http://google.com/?#q="

term=input("Enter search query")

#webbrowser.open(tabUrl+term,new=new)

quote_page=(tabUrl+term)

#webbrowser.open(quote_page)

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
#name_box = soup.find('div',attrs={"class":"rc"}).findAll('h3')
#name_box = soup.find('h3', attrs={'class': 'r'})
#name = name_box.text.strip()
# strip() is used to remove starting and trailing
#print (name)
#print name_box[2].find('strong').string

#webbrowser.open(quote_page)

name_box = soup.find_all("div", attrs={ "class" : "rc" })
#names = name_box.findAll('h3')
#for name in name_box
print (name_box)
