import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
def Htmlurl(url):
	try:
		r.requests.get(url,headers=headers)
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return None

def getmessage(html):
	try:
		html = BeautifulSoup(html,'lxml')
		all_a = html.find('div',class_=row).find_all('h2')
		for message in all_a:
			alink = message.select('a')
			ruwei = str(alink)
			print("OK!",alink)
	except:
		print("No")

def main():
	url_message = "https://pyname.com/page/"
	for i in range(1,142):
		try:
			url = url_message + str(i)
			html = Htmlurl(url)
			getmessage(html)
		except:
			continue
main()
