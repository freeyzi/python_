import requests
from bs4 import BeautifulSoup

#for link in soup.find_all('a'):
#   print(link.get('href'))

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
print(demo)