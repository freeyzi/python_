#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()#声明浏览器对象
try:
    browser.get('https://www.baidu.com') #传入url，跳出浏览器访问url
    input = browser.find_element_by_id('kw')#查找id为kw的元素
    input.send_keys('垃圾百度！')#赋值input,调用send_keys，向元素发送键
    input.send_keys(Keys.ENTER) #敲入回车
    wait = WebDriverWait(browser, 20)#调用等待元素被加载
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))#等待一个content_left元素被加载
    print(browser.current_url)#打印当前url
    print(browser.get_cookies())#打印cookie
    print(browser.page_source)#打印源代码
finally:
    browser.close()#最后关掉浏览器