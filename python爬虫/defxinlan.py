from pyquery import PyQuery as pq

def xinlang():
	try:
		doc = pq('https://mil.news.sina.com.cn/',encoding="utf-8")
		htmls = doc('.wrap .zgjq ul li a')
		for html in htmls.items():
			href = html.attr('href')
			text = html.text()
			heers = href + '\n' + text
			print(heers)

			with open("新浪.txt",'a',encoding="utf-8") as f:
				f.write(heers)
				f.close()
	except:
		print("====.====")

def main():
	xinlang()
main()