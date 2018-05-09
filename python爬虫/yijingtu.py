import requests
from bs4 import BeautifulSoup
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
'''http://www.yeitu.com/ # 亿图全景图库'''

url = "http://www.yeitu.com/tag/zuoji_toxic/"
if not os.path.isdir("Toxic"):  # 如没有Toxic文件夹则新建一个
    os.mkdir("Toxic")


def response(url):
    html = str(requests.get(url, headers=headers,timeout=5).content, "utf-8")
    soup = BeautifulSoup(html, "lxml")
    return soup


def download(url, f_path):
    soup = response(url)
    res_list = soup.select(".img_box img")
    for res in res_list:
        # print(res.get("src"))
        try:
            pic = requests.get(res.get("src"))
        except requests.ConnectionError:
            print("【错误】图片无法下载！！！")
        file_name = (res.get("src")).split("/")[-1].replace("?imageslim", "")
        file_path = f_path + "\\" + file_name
        if os.path.isdir(file_path):
            print("【错误】-文件已存在...")
            break
        else:
            with open(file_path, "wb") as fp:
                fp.write(pic.content)
            print("进程", os.getpid(), "【下载完成】-", file_name)


# 读取下一页的链接
def next_pages(url, file_path):
    soup = response(url)
    last_page = soup.select("#pages a")[10].get("href")
    lp = str(last_page).split("_")[-1][0:2]  # 读取最后一页
    # return lp
    for i in range(1, int(lp) + 1):
        if i == 1:
            page = url
        else:
            page = url.split(".html")[0] + "_" + str(i) + ".html"
        download(page, file_path)


# 读取图集目录
def res_html(url):
    if not url == None:
        soup = response(url)
        for res in soup.select(".title a"):
            file_path = "Toxic" + "\\" + res.text
            if not os.path.isdir(file_path):
                os.mkdir(file_path)
            print(res.get("href"), file_path)
            next_pages(res.get("href"), file_path)


if __name__ == "__main__":
    res_html(url)
    print("【全部图片完成下...】")