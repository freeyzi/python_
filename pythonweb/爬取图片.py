from pyquery import PyQuery as pq
import requests
import os


for i in range(1,18):
	url = "http://www.xiao688.com/cms/article/id-82834_page-" + str(i) + ".html"
	print(url)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36"}

def HtmlUrl(url):
    try:
        response = requests.get(url,headers=headers,timeout=10).content.decode()
        doc = pq(response)
        html_image = doc('.longConWhite ul li img')
        print(html_image)
        for html in html_image.items():
            images = html.attr.src
            print(images)
            url = images
            root = "D://picsss//"  # 定义根目录
            path = root + url.split('/')[-1]
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path + '.jpg', 'ab') as f:
                    f.write(r.content)  # 二进制格式保存为文件
                    f.close()
                    print("文件保存成功")
            else:
                print("文件保存失败")
    except:
        print("爬取失败")
def main():
    for i in range(2,34):
        url = 'http://www.59pic.com/mn/1284_' + str(i) + '.html'
        HtmlUrl(url)
main()