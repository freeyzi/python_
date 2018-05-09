import requests
import re
import traceback
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r = requests,get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return None

def getStockList(lst,stocKURL):
	html = getHTMLText(stocKURL)
	soup = BeautifulSoup(html,'html.parser')
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
			continue

def getStockInfo(lst, stocKURL, fpath):
	for stock in lst:
		url = stocKURL + stock + ".html"
		html = getHTMLText(url)
		try:
			if html=="":
				continue
			infoDict = {}
			soup = BeautifulSoup(html,'lxml')
			stockInfo = soup.find('div',attrs={'class':'stock-bets'})

			name = stockInfo.find_all(attrs={'class':'bets-name'})
			infoDict.update({'股票名称':name.text.split()[0]})

			keyList = stockInfo,find_all('dt')
			valuelist = stockInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[i].text
				val = valuelist[i].text
				infoDict[key] = val

			with open(fpath,'a',encoding="utf-8") as f:
				f.write( str(infoDict) + "\n")
		except:
			traceback.print_exc()
			continue

def main():
	stock_list_url = 'https://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = 'D:/baidustockInfo.txt'
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)
main()