import requests
from lxml import etree
from pyquery import PyQuery as pq

doc  = pq('https://mil.news.sina.com.cn/',encoding="utf-8")
html = doc('.wrap a')
for htmls in html.items():
	href = htmls.attr('href')
	text = htmls.text()
	heerweiyi = href + '\n' + text
	print(heerweiyi)

	with open('xinlang.txt','a',encoding="utf-8") as f:
		f.write(heerweiyi + "\n")

