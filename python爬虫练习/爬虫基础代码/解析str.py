import requests

r = requests.get("http://hpptbin.org/get")
print(r.json())