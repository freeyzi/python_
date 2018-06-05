import requests
import os
url = "https://teddysun.com/wp-content/uploads/2014/shadowsocks.png"
root = "D://pics//" #定义根目录
path = root + url.split('/')[-1] #标识文件路径为root,url链接以反/分割的最后一部分为名字
try:
    if not os.path.exists(root): #判断根目录是否存在，不存在就建立根目录
        os.mkdir(root)
    if not os.path.exists(path): #判断文件是否存在，当文件不存在，通过request.get方式从网上获取相关的文件
        r = requests.get(url) #
        with open(path,'wb') as f:
            f.write(r.content) #二进制格式保存为文件
            f.close()
            print("文件保存成功")
    else:
        print("文件保存失败")
except:
    print("爬取失败")