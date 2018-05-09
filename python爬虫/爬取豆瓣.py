import requests
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

def get_url(url):
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		return response.text
	return None

def parse_url(html):
	htmls = etree.HTML(url)
	url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")



def main():
	url = "https://movie.douban.com/chart"
	html = get_url(url)
	for url_lists in parse_url(html):
	print(url_lists)
main()