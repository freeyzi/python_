import requests
import json
import pymongo
 
conn = pymongo.MongoClient(host='localhost',port=27017)
toutiao = conn['toutiao']
newsdata = toutiao['news']
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = requests.get(url,headers=headers,timeout=10).text
print(wbdata)
data = json.loads(wbdata)
news = data['data']['pc_feed_focus']
for n in news:
    title = n['title']
    img_url = n['image_url']
    url = n['media_url']
    data = {
        'title':title,
        'img_url':img_url,
        'url':url
    }
    newsdata.insert_one(data)
for i in newsdata.find():
    print(i)