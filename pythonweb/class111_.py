import requests
from pyquery import PyQuery as pq
from lxml import etree
import json

def get_html_request(url):
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"}
    response = requests.get(url,headers=headers,timeout=10).content.decode()
    return response

def get_html_list(url_list):
    doc = pq(url_list)
    htmls = doc('.article-catlist h4 a')
    content_list = []
    for html in htmls.items():
        item = {}
        item["title"] = html.text()
        item["url"] = html.attr('href')
        content_list.append(item)
    return content_list

def get_html_save(url_saves):
    with open('D:\\chinaz3.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(url_saves,ensure_ascii=False))
        f.write('\n')
        f.close()
        print('保存：',url_saves)

def main():
    url = 'https://www.chinaz.com/news/roll/3.shtml'
    html_url = get_html_request(url)
    html_list = get_html_list(html_url)
    html_save = get_html_save(html_list)
main()