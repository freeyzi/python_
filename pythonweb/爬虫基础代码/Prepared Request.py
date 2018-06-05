from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}

headers = {"...."}

s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
#将请求表为数据结构，每个参数都可以通过一个为Request对象来表示
#先引入Request，然后用url,data和headers参数构造一个Request对象，这时需要在调用Session的prepare_request（）的方法将其转换为Prepared Request对象，然后调用send()方法发送即可