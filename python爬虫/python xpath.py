from lxml import etree
import requests

url = "https://movie.douban.com/chart"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
response = requests.get(url,headers=headers)
html_str = response.content.decode()
#使用etree处理数据

html = etree.HTML(html_str)
url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")
print(url_list)

img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
print(img_list)

