from pyquery import PyQuery as pq
import requests

class Dongman():
    def __init__(self):
        self.url_temp = "http://www.qzone.cc/qqtouxiang/katong/list_{}.html"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36"}

    def get_url_list(self):
        url_list = [self.url.url_temp.format(i) for i in range(1,11)]
        return url_list

    def pase_url(self,url):
        print("抓取:",url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):
        doc = pa(html_str)
        images = doc('.newtxList ul li a img')
        for image in images.items():
            html_image = image.attr.src
            print(html_image)
        return html_image

    def save_content_list(self,content_list):
        with open("katong.txt",'a',encoding='utf-8') as f:
            f.write(content)
            f.write('\n')
            f.close()

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.pase_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)

if __name__ == '__main__':
    don = Dongman()
    don.run()

