import requests
url = "https://item.jd.com/2967929.html"
try:
    kv = {"user-agent":"Mozilla/5.0"}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    print(r.request.headers)
except:
    print("爬取失败！")

