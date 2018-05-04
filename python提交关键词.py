import requests
keyword = "python"
try:
    kv = {"wd":keyword}
    r = requests.get("http://www.baidu.com/s",params=kv) #向百度提交关键词
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败！")

