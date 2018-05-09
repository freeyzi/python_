import requests
from bs4 import BeautifulSoup
import os

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
	}

url = "http://www.mzitu.com/78538/2"
html_url = requests.get(url,headers=headers).content.decode()
soup = BeautifulSoup(html_url,'lxml')
all_a = soup.find('div',class_='main-image').find('a')
r = all_a.get(all_a)
with open('favicon.jpg','wb') as f:
    f.write(all_a.content)