import requests

r = requests.get("https://www.baidu.com")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

#调用cookies属性得到cokies,然后用items()方法转换元组组成的列表