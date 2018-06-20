import requests
from pyquery import PyQuery as pq 
import os


class Images:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"}
        self.url_tmp = "http://www.banana-project.com/news/list-1-1.html"

    def get_url(self,url):
        response = requests.get(url,headers=self.headers,timeout=10)
        return response.content.decode()

    def get_url_list(self,url_html):
        doc = pq(url_html)
        imagess = doc('.list-right ul li p a img')
        for htmll in imagess.items():
            href = "http://www.banana-project.com" + htmll.attr.src
        return href

    def get_url_save(self,url_list):
        url = url_list
        root = "D:\\picssimg\\"
        path = root + url.split('/')[-1]
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'ab') as f:
                f.write(r.content)
                f.close()
                print("0.0")

    def run(self):
        url = self.url_tmp
        url_html = self.get_url(url)
        url_list = self.get_url_list(url_html)
        self.get_url_save(url_list)

if __name__ == '__main__':
    img = Images()
    img.run()