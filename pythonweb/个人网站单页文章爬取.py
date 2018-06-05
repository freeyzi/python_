from pyquery import PyQuery as pq

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36"}
def Htmlurl(url):
	try:
		print("爬取中：")
		doc = pq(url,headers=headers,timeout=5,encoding='utf-8')
		html_titles = doc('.row h1')
		html_title = html_titles.text()
		print(html_title)
		html_texts = doc('.row .entry-content p')
		html_text = html_texts.text()
		message = html_title + "\n" + html_text
		return message
	except:
		print("爬取失败")
def Save(html):
	try:
		with open('D:\\python\\入微.txt','w',encoding='utf-8') as f:
			f.write(html)
			f.close()
			print('保存成功')
	except:
		print("保存失败！")

def main():
	url = "https://pyname.com/2018/04/820"
	html = Htmlurl(url)
	htm = Save(html)

main()