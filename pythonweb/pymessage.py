import requests
from lxml import etree
from pyquery import PyQuery as pq
import unittest

class Douban:
    def __init__(self):
        self.urls = "https://www.chinaz.com"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}

    def get_message(self,url):
        response = requests.get(url,headers=self.headers,timeout=10)
        return response.content.decode()

    def get_save(self,html_url):
        with open("D:\\list.txt",'w',encoding='utf-8') as f:
            f.write(str(html_url))
            f.write('\n')
            f.close()

    def run(self):
        url = self.urls
        html_url = self.get_message(url)
        self.get_save(html_url)

if __name__ == '__main__':
    dou = Douban()
    dou.run()

unittest.main()
