import requests
from bs4 import BeautifulSoup
import csv

URL="https://gadgets.ndtv.com/news"
r=requests.get(URL)

soup=BeautifulSoup(r.content,'html5lib')

recent_news_widget=[]
table=soup.find('div',attrs={'class':'recent_news_widget'})

for row in table.findAll('div',attrs={'class':'recent_news_widget'}):
	news={}
	news['title']=row.text
	recent_news_widget.append(news.text)

filename='tech_news.csv'
with open(filename,'w') as file:
	writer=csv.DictWriter(file,['title'])
	writer.writeheader()
	for news in recent_news_widget:
		writer.writerow(news)


