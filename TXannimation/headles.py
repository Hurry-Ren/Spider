'''
腾讯动漫的加载是异步加载，不要一次性把滚动条拖完，一下子全部拖完可能加载不到这么多数据
可以设置间距多加载几次次（见下）
'''

from selenium import webdriver  # 导入selenium的浏览器驱动接口
import time
import re
from lxml.html import etree
import urllib.request


firefox_options = webdriver.FirefoxOptions()  # 创建firefox参数对象
firefox_options.add_argument('--headless')  # 把firefox设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
driver = webdriver.Firefox(firefox_options = firefox_options)  # 创建firefox无界面对象
driver.maximize_window()    #窗口最大化

for i in range(1,10):
    url = 'https://ac.qq.com/ComicView/index/id/531490/cid/'+str(i)
    driver.get(url=url)
    time.sleep(2)
    print(url)
    # 拖动到指定元素位置
    try:
        for j in range(20):
            targetElem = driver.find_element_by_xpath('//*[@id="comicContain"]/li[' + str(j + 4) + ']/div[1]')
            driver.execute_script("arguments[0].scrollIntoView();", targetElem)
            time.sleep(3)
    except Exception as err:
        pass

    # 找最后一次的加载点
    targetElem = driver.find_element_by_xpath('//*[@id="mainControlNext"]/span')
    driver.execute_script("arguments[0].scrollIntoView();", targetElem)
    time.sleep(2)

    #找数据(用xpath进行选择)
    url = []
    try:
        data = etree.HTML(driver.page_source)
        url = data.xpath('//ul[@id="comicContain"]/li/img/@src')
    except Exception as err:
        print("数据读取出错！")
    for k in range(0,len(url)):
        urllib.request.urlretrieve(url[k],'D:/animation/animation'+str(i)+'_'+str(k) +'.png')
        time.sleep(1)
        # fh = open(, 'w', encoding='utf-8')
        # fh.write(targetUrl)
        # fh.close()
driver.close()
