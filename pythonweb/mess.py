import requests
from lxml import etree
from pyquery import PyQuery as pq
import os
import re
import json

class Xianni:

    def __init__(self):
        self.url_tmp = "https://www.qu.la/book/633/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"}

    def get_html(self,url):
        try:
            response  = requests.get(url,headers=self.headers,timeout=10)
            return response.content.decode()
        except:
            return None

    def get_list(self,message):
        try:
            doc = etree.HTML(message)
            html = doc.xpath("//div[@id='list']")
            contentlist = []
            for div in html:
                items = {}
                items['title'] = div.xpath(".//dl//dt//text()")
                items['href'] = div.xpath(".//dl//a//@href")
                items['text'] = div.xpath(".//dl//a//text()")
                contentlist.append(items)
            return contentlist
        except:
            return None

    def get_pyquery(self,message):
        try:
            doc = pq(message)
            html = doc('#list dl dd a')
            conpyquery = []
            for lists in html.items():
                items = {}
                items['text'] = lists.text()
                items['href'] = "https://www.qu.la" + lists.attr('href')
                conpyquery.append(items)
            return conpyquery
        except:
            return None

    def get_save(self,doc):
        try:
            with open('D:\\xianni.txt','a',encoding='utf-8') as f:
                f.write(str(doc))
                f.write('\n')
                f.close()
                print('2333')
        except:
            return print("lxml no")

    def get_pysave(self,pyqu):
        try:
            with open("D:\\xinanni2.txt",'a',encoding='utf-8') as f:
                f.write(str(pyqu))
                f.write('\n')
                f.close()
                print('2333')
        except:
            return print("pyquery no!")

    def run(self):
        url = self.url_tmp
        message = self.get_html(url)
        doc = self.get_list(message)
        pyqu = self.get_pyquery(message)
        self.get_save(doc)
        self.get_pysave(pyqu)

if __name__ == '__main__':
    xian = Xianni()
    xian.run()