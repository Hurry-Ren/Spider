from selenium import webdriver
import time
from CSDN import account

'''
这是使用selenium的版本
'''
option = webdriver.FirefoxOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
option.add_argument(user_agent)
driver = webdriver.Firefox(options=option)

driver.get('https://passport.csdn.net/login?code=public')
time.sleep(2)

#通过账号密码登陆           （失败，遇到了滑块验证）
account.account(driver)

#通过手机验证码登陆         （失败，遇到了滑块验证）
#iphone.phone(driver)

# data = driver.page_source
# fh = open('D:/animation/CSDN.txt','w',encoding='utf-8')
# fh.write(data)
# fh.close()
img = driver.save_screenshot('D:/animation/CSDN.png')
driver.close()
#//*[@id="all"]

#抓包分析下账号登陆的地址是哪个(没分析出来，直接用点击事件)
