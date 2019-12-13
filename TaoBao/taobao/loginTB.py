from pyppeteer.launcher import launch
import asyncio
import random
from TaoBao.taobao.spider_img import set_cookie
from TaoBao.taobao.argus import argus


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
async def main(name,pwd,url):
    try:
        brower = await launch(argus())
        page = await brower.newPage()
        await page.setUserAgent(user_agent)
        # 下面这个属性必须要
        await page.evaluateOnNewDocument(
            '''() =>{ Object.defineProperties(navigator, { webdriver: { get: () => undefined} }) }''')
        await page.goto(url)
        await asyncio.sleep(2)
        # 找到'账号密码'页面键
        btn1 = await page.xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]')
        await btn1[0].click()
        await asyncio.sleep(2)
        # 账号
        user_name = await page.xpath('//*[@id="TPL_username_1"]')
        await user_name[0].type(name, {'delay': random.randint(100, 151) - 50})
        await asyncio.sleep(2)
        # 密码
        user_pwd = await page.xpath('//*[@id="TPL_password_1"]')
        await user_pwd[0].type(pwd, {'delay': random.randint(100, 151) - 50})
        await asyncio.sleep(2)

        # 登陆键
        btn2 = await page.xpath('//*[@id="J_SubmitStatic"]')
        await btn2[0].click()
        await asyncio.sleep(10)
    except Exception as err:
        print(err)

    await get_cookie(page)
    await page.close()

# 获取登录后cookie
async def get_cookie(page):
    try:
        # res = await page.content()
        cookies_list = await page.cookies()
        cookies = ''
        for cookie in cookies_list:
            str_cookie = '{0}={1};'
            str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
            cookies += str_cookie
        await set_cookie(cookies)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    user_name = ''
    user_pwd = ''
    url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d95jSEOT&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
    loop = asyncio.get_event_loop()  #协程，开启个无限循环的程序流程，把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
    loop.run_until_complete(main(user_name,user_pwd,url))  #将协程注册到事件循环，并启动事件循环

