import requests
from pyquery import PyQuery as pq
import unittest

class Qiushibaike:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
                        "Host":"www.qiushibaike.com",
                        "If-None-Match":"e3c65b5581b90df204bc13d0527e710a153a9a3a"}
        self.urls = "https://www.qiushibaike.com/text/page/{}/"

    def get_url_page(self):
        url_list = [self.urls.format(i) for i in range(1,15)]
        print(url_list)
        return url_list

    def get_url_html(self,url):
        response = requests.get(url,headers=self.headers,timeout=10).content.decode()
        return response

    def get_url_list(self,html_str):
        doc = pq(html_str)
        html = doc('.col1 a .content span')
        for i in html.items():
            text = i.text() + '\n'
            return text

    def get_message_save(self,get_html_list):
        with open("D:\\糗事百科.txt",'a',encoding='utf-8') as f:
            f.write(str(get_html_list))
            f.write('\n')
            f.close()
            print(">>>",get_html_list)

    def run(self):
        url_list = self.get_url_page()
        for url in url_list:
            html_str = self.get_url_html(url)
            get_html_list = self.get_url_list(html_str)
            self.get_message_save(get_html_list)

if __name__ == '__main__':
    qiubai = Qiushibaike()
    qiubai.run()

unittest.main()