from pyquery import PyQuery as pq
import requests
import os

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"}

def Html(url):
	print(url)
	response = requests.get(url,headers=headers).content.decode()
	doc = pq(response)
	html_list = doc('.pMain a img')
	for image in html_list.items():
		href = image.attr.src
		href_get = "http:" + href
		print(href_get)
		url = href_get
		root = "D://touxiangs//" #定义根目录
		path = root + url.split('/')[-1] #标识文件路径为root,url链接以反/分割的最后一部分为名字
		try:
			if not os.path.exists(root): #判断根目录是否存在，不存在就建立根目录
				os.mkdir(root)
			if not os.path.exists(path): #判断文件是否存在，当文件不存在，通过request.get方式从网上获取相关的文件
				r = requests.get(url) #
				with open(path+'.jpg','ab') as f:
					f.write(r.content) #二进制格式保存为文件
					f.close()
					print("文件保存成功")
			else:
				print("文件保存失败")
		except:
			print("爬取失败")

def main():
	for i in range(1,318):
		url = 'https://www.woyaogexing.com/touxiang/katong/index_' + str(i) + '.html'
		print(url)
		Html(url)
main()