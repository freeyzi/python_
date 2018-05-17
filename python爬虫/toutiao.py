import requests
import json
import pymongo
 
conn = pymongo.MongoClient(host='localhost',port=27017)
toutiao = conn['toutiao']
newsdata = toutiao['news']
 
url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = requests.get(url).text
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