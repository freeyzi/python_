import requests
import logging
#捕获警告到日志的方式忽略警告
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn',verify=False)  #设置verify参数为false
print(response.status_code)