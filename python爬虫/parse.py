import requests
from retrying import retry

'''
专门请求url地址的方法
'''

#伪装浏览器访问服务器
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
          "Referer": "http://fanyi.baidu.com/?aldtype=16047"}
@retry(stop_max_attempt_number=3) #下面的程序反复执行三次，三次全被报错才会报错，中间有一次正常，程序继续往后走
def __parse_url(url):
    print("*"*100) #+出现
    response = requests.get(url,headers=headers,timeout=5) #5秒之内必须返回响应，否则报错
    return response.content.decode() #如果没有报错，返回响应的字符串

def parse_url(url):
    try:
        html_str = __parse_url(url)
    except:
        html_str = None  #如果报错就返回一个None值，不为None就访问成功
    return html_str

#访问成功
if __name__ == '__main__':
    url = "http://www.baidu.com/" #这个不报错
    url1 = "www.baidu.com"  #这个报错
    print(parse_url(url1))

