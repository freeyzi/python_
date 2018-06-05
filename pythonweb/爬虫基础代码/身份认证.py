import  requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:50000',auth=HTTPBasicAuth('username','password'))
print(r.status_code)

#如果用户名密码正确，就会自动认证跳转，返回200状态码，否则401

#简写：
import  requests
r = requests.get('http://localhost:50000',auth=('username','password'))
print(r.status_code)