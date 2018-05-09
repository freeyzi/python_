import requests
#目标地址
url = "http://fanyi.baidu.com/basetrans"
zidian = { "query": "啊哈哈哈哈哈",
            "from": "zh",
            "to": "en" }
#模拟浏览器
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
          "Referer": "http://fanyi.baidu.com/?aldtype=16047"}

response = requests.post(url,data=zidian,headers=headers)
print(response)
print(response.content.decode())

@retry(stop_max_attempt_number=3) #以下函数执行三次，报错三次就报错，有一次通过就不报错
def fun1():
    print("this is fun1")
    raise ValueError("this is test error")