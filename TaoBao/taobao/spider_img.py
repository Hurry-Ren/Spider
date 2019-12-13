import re
from selenium import webdriver
import time
from lxml.html import etree

url = 'https://s.taobao.com/search?q=%E7%94%B5%E8%84%91'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
#爬取淘宝商品图片
def set_cookie(cookies):
    pat = '(.*?)=(.*?);'
    cookie2 = re.compile(pat).findall(cookies)
    spider_img(cookie2)

def spider_img(cookie):
    brower = webdriver.FirefoxOptions()
    brower.add_argument(user_agent)
    driver = webdriver.Firefox(firefox_options = brower)
    driver.maximize_window()
    driver.add_cookie(cookie)
    driver.get(url)
    time.sleep(2)

    data = etree.HTML(driver.page_source)
    shap_name = data.xpath('//*[@id="J_Itemlist_TLink_532208258584"]')
    print(shap_name)

    driver.close()



