import requests

#http代理和https代理
proxies = {
    "http":"http://10.10.1.10:2128",
    "https":"https://10.10.1.10:1080",
    "http":"http://user:password@10.10.1.10:1080/",
}

requests.get("https://www.taobao.com",proxies=proxies)

#socks协议代理

#安装socks库：pip3 install 'requests[socks]'

proxies = {
    "http":"socks5://user:password@host:post",
    "https":"socks5://user:password@host:post",
}
requests.get("https://www.taobao.com",proxies=proxies)
