#these are the python libraries which are used to extract data out of HTML files
import requests
from bs4 import BeautifulSoup
import csv


URL="https://gadgets.ndtv.com/news"	 #url of the website used for we scrapping
r=requests.get(URL)
#web scrapping is checked to be legalised on this website


soup=BeautifulSoup(r.content,'html5lib')
# We create a BeautifulSoup object by passing two arguments

tech_news=[]	#list for storing tech news
table=soup.find('div',attrs={'class':'recent_news_widget'})
#find() returns the first matching element through the argument passed

for row in table.findAll('li',attrs={'data-tb-region-item'}):
	#tech news is stored in the list 'data-tb-region-item'
	news={}
	news['title']=row.text
	tech_news.append(news.text)

filename='tech_news.csv'    	#create a csv file to store output

with open(filename,'w') as file:
	writer=csv.DictWriter(file,['title'])
	writer.writeheader()
	
	for news in tech_news:
		writer.writerow(news)


