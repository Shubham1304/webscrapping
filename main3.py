#import urllib
import urllib.request as urllib2 

from bs4 import BeautifulSoup

quote="https://www.accuweather.com/en/in/india-weather"

page=urllib2.urlopen(quote)

soup=BeautifulSoup(page,'html.parser')

#print(soup.prettify())
print('\n')
print(soup.title.string)
print('\n')
print(soup.body)

