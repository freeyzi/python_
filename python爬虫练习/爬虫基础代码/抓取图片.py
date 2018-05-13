import requests

r = requests.get("http://mm.chinasareview.com/wp-content/uploads/2017a/07/11/01.jpg")
with open('favicon.jpg','ab') as f:
    f.write(r.content)
