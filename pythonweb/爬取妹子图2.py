import requests
from bs4 import BeautifulSoup
import os

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
	"Referer":"http://www.mzitu.com/all/"
}
all_url = "http://www.mzitu.com/all"
staet_html = requests.get(all_url,headers=headers)
Soup = BeautifulSoup(staet_html.text,'lxml')##使用BeautifulSoup解析获取到的网页
all_a = Soup.find('div',class_='all').find_all('a')
for a in all_a:
	title = a.get_text()#取出a标签
	href = a['href'] #取出a标签的href属性
	html = requests.get(href,headers=headers)
	html_Soup = BeautifulSoup(html.text,'lxml')
	#查找所有的span标签，获取第十个span标签中的文本也就是最后一个页面了
	max_span = html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
	for page in range(1,int(max_span)+1):
		page_url = href + '/' + str(page)
		img_html = requests.get(page_url,headers=header)
		img_Soup = BeautifulSoup(img_html.text,'lxml')
		img_url = img_Soup.find('div',class_='main-image').find('img')['src']
		name = img_url[-9:-4]#取url,倒数第四至第九位做图片名字
		img = requests.get(img_url,headers=headers)
		f = open(name+'.jpg','ab') #写入文件用b参数
		f.write(img.content)
		f.close()