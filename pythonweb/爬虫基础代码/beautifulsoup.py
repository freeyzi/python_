import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html").text
suop = BeautifulSoup('<p>data</p>','html.parser')
print(suop.prettify())