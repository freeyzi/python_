import json
import requests
import pymongo

conn = pymongo.MongoClient(host='localhost',port=27017)
toutiao = conn['douban']
newsdata = toutiao['video']

url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=10&page_start=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
        'Referer':'https://movie.douban.com/tv/'}
response = requests.get(url,headers=headers).content.decode()
data = json.loads(response)
news = data['subjects']
for n in news:
    rate = n['rate']
    title = n['title']
    url = n['url']
    data = {
    'rate':rate,
    'title':title,
    'url':url
    }
    newsdata.insert_one(data)
for i in newsdata.find():
    print(i)