import requests
from lxml import etree

url = "https://pyname.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
response = requests.get(url,headers=headers).content.decode()
html = etree.HTML(response)
html_text = html.xpath("//div[@class='site']//div[@id='primary']//h2/a/text()")
print(html_text)
html_texts = html.xpath("//div[@class='site']//div[@id='primary']//h2/a/@href")
print(html_texts)


