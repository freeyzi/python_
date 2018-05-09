import requests
url = "http://www.renren.com/965507033/profile"
#cookie放在headers中
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
           "Referer": "http: // zhibo.renren.com / top",
           "Cookie":"anonymid=jgaqqru8-nfncif; depovince=GW; _r01_=1; JSESSIONID=abc1la9uG61Mp41_4jTlw; ick_login=137ddf62-0330-454d-b92a-f2b4a5aeaef4; ick=325289cb-be89-4762-8fc5-5dc991ac6b3e; t=8c3106b387e0a11b89c73a77db923a9c3; societyguester=8c3106b387e0a11b89c73a77db923a9c3; id=965507033; xnsid=12d288e0; XNESSESSIONID=3a5a4bb9eed9; ch_id=10050; wp_fold=0; jebecookies=39ccf3e0-550d-47aa-8546-1a0af54454ac|||||"}
response = requests.get(requests(url,headers=headers)

with open("htmls.html","w",encoding="utf-8") as f:  #抓取登陆后的页面保存到本地
    f.write(response.content.decode())