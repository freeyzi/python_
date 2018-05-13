from pyquery import PyQuery as pq
import requests
import os

#for i in range(1,18):
#	url = "http://www.xiao688.com/cms/article/id-82834_page-" + str(i) + ".html"
#	print(url)
url = "https://www.aitaotu.com/zt/mntp/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36"}
doc = pq(url,headers=headers,timeout=10)
html_image = doc('#maincont dd a img')
print(html_image)
for html in html_image.items():
	images = html.attr.img
	print(images)
	url = images
	root = "D://pics//" #定义根目录
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