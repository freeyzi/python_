from pyquery import PyQuery as pq
import requests
import os

f = open('sss.txt','r')
for lien in f:
    urls = lien.rstrip()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36"}
url = urls
response = requests.get(url,headers=headers,timeout=10)
doc = pq(response.text)
html_titles = doc('.bookname h1')
html_messages = doc('#content')
html_title = html_titles.text()
html_message = html_messages.text().rstrip()
heer = html_title + '\n' + html_message
urls = heer
root = "D://touxiangs//" #定义根目录
path = root + urls.split('/')[-1] #标识文件路径为root,url链接以反/分割的最后一部分为名字
try:
    if not os.path.exists(root): #判断根目录是否存在，不存在就建立根目录
        os.mkdir(root)
    if not os.path.exists(path): #判断文件是否存在，当文件不存在，通过request.get方式从网上获取相关的文件
        r = requests.get(url) #
        with open(path+'.txt','wb') as f:
            f.write(r) #二进制格式保存为文件
            f.close()
            print("文件保存成功")
    else:
        print("文件保存失败")
except:
    print("爬取失败")
