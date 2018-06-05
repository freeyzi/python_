import requests
from lxml import etree

url = "https://zhuanlan.zhihu.com/p/34545910"
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36",
	}

response = requests.get(url,headers=headers,timeout=5).content.decode()
html = etree.HTML(response)
html_titles= html.xpath("//div[@class='App']//header[@class='Post-Header']/h1/text()")
for html_title in html_titles:
	print(html_title)
html_textes = html.xpath("//div[@class='App']//div[@class='RichText Post-RichText']//p/text()")
for html_texte in html_textes:
	print(html_texte)
