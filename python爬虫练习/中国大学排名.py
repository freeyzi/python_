import requests
from bs4 import BeautifulSoup
import bs4

#输入是获取url信息，输出是url内容,返回给其他程序
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30) #获取url信息,超时是30秒
        r.raise_for_status() #产生异常信息
        r.encoding = r.apparent_encoding #修改编码  #将网页的信息内容返回给程序的其他部分
        return r.text
    except:
        return None
    return

#将一个html页面放到一个listl列表中，列表定义为ulist
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'lxml')
    #采用for语句,查找html文本中的tbody标签,并且将他的孩子children做一个遍历
    for tr in soup.find('tbody').children:
        #检测tr标签的类型,如果类型不是bs4库定义的Tag类型，将过滤掉
        if isinstance(tr,bs4.element.Tag):
            #对td标签查询
            tds = tr('td')
            #将td标签存为列表类型tds,在ulist中增加需要的对应字段，分别是大学排名，大学名称，大学排分
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

#将ulist列表打印
def printUnivList(ulist,num):
    #打印大学信息，大学信息包含表头
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))

def main():
    # 将大学信息放到列表中
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    #分别调取三个步骤对应的函数
    #将url转换为html
    html = getHTMLText(url)
    #然后将html信息提取后放在fillUnivList变量中
    fillUnivList(uinfo,html)
    #打印大学信息
    printUnivList(uinfo,310) #列出20所学校信息
main()


