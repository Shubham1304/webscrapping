#import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

#specification of url
quote_page='https://www.accuweather.com/en/in/india-weather'

# query the website and return the html to the variable ‘page’
page=urllib2.urlopen(quote_page)


soup=BeautifulSoup(page,'html.parser')

name_box1=soup.find('h6',attrs={'<href : https://www.accuweather.com/en/in/ahmedabad/202438/weather-forecast/202438'})
name1=name_box1.text.strip()

#name_box2=soup.find('a',attrs={'href':'/en/us/miami-fl/33128/weather-forecast/347936'})
#name1=name_box1.text.strip()

#name_box3=soup.find('a',attrs={'href':'/en/us/los-angeles-ca/90012/weather-forecast/347625'})
#name1=name_box1.text.strip()

temp_box1=soup.find('span',attrs={'class':'large-temp'})
temp1=temp_box1.text

#temp_box2=soup.find('span',attrs={'class':'large-temp'})
#temp1=temp_box1.text

#temp_box3=soup.find('',attrs={})
#temp1=temp_box1.text

print(name1)
print(temp1)

# open a csv file with append, so old data will not be erased
with open('index2.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([temperature, datetime.now()])
