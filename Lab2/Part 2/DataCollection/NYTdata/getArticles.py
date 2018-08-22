from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import requests
api = articleAPI("458e6335355c4f2fb83770f41baa4309")
f=open('nytArticles.txt','w')
links=[]
try:
    for a in range(0,20):
        articles = api.search(q="shooting", begin_date=20180406,end_date=20180407,page=a)
        for i in range(0,len(articles['response']['docs'])):
            url = articles['response']['docs'][i]['web_url']
            data = requests.get(url)
            soup = BeautifulSoup(data.content, 'html.parser')
            soup.prettify()
            for j in range((len(soup.find_all('p')))-3):
                f.write(soup.find_all('p')[j].get_text())

            #print(url)
            links.append(url)
    f.close()
except:
    print("We got only",len(links)," articles for selected period")
