import requests

#实例化session
session = requests.session()

#使用session发送post请求，获取对方保存在本地的cookie
post_url = "https://pyname.com/wp-jita.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36" }
post_data = {"log":"whoisit","pwd":"www.google.com"}
session.post(post_url,headers=headers,data=post_data)

#在使用session请求登陆后的页面
url = "https://pyname.com/wp-admin/"
response = session.get(url,headers=headers)

with open("renren3.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())