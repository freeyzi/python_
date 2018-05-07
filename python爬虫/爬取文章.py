import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
try:
    for i in range(1,142):

        url = 'https://pyname.com/page/' + str(i)
        response = requests.get(url, headers = headers)
        html = BeautifulSoup(response.text, 'lxml')
        all_a = html.find('div', class_='row').find_all('h2')
        for all_all in all_a:
            alink = all_all.select('a')
            ruwei = str(alink)
            print("保存成功",alink)
            with open('ruwei.html','a',encoding="utf-8") as f:
                f.write(str(alink) + "\n")
                f.close()
                print("保存成功")
except:
    print("抓取失败")