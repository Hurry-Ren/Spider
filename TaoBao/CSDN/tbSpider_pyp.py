'''
这是使用pyppeteer的版本（绕过webdriver 检测）
下面的代码有时候成功，有时候不成功。
可能和ip有关
'''
import asyncio
from pyppeteer.launcher import launch
import time,random

width,height = 1366,768
async def main():
    # executablePath = pathtochrome,
    # pathtochrome = 'C:\\Users\\asus\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
    # brower = await launch(headless = False,
    #                       args=[f'--window-size={width},{height}'],
    #                       dumpio = True,
    #                     )
    brower = await launch({
        'headless': False,
        'dumpio': True,
        'args': [
            '--disable-extensions',
            '--hide-scrollbars',
            '--disable-bundled-ppapi-flash',
            '--mute-audio',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            '--disable-infobars',
            #'--proxy-server=119.123.179.200:9090',
        ],
    })

    page = await brower.newPage()
    await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11')
   # 本页刷新后值不变
    await page.evaluateOnNewDocument('''() =>{ Object.defineProperties(navigator, { webdriver: { get: () => undefined} }) }''')
    # await page.evaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, { plugins: { get: () => [0, 1, 2]} }) }''')
    # await page.evaluateOnNewDocument('''() =>{ Object.defineProperty(navigator, { languages: { get: () => ["zh-CN", "zh", "en"]} }) }''')
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://passport.csdn.net/login?code=public')
    #用以下方法后window.navigator.webdriver只是临时改变，刷新页面后又会变回去
    # await page.evaluate(
    #     '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # await page.evaluate(
    #     '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    # await page.evaluate(
    #     '''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    time.sleep(2)

    but1 = await page.xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a')
    await but1[0].click()
    time.sleep(3)

    sel1 = await page.xpath('//*[@id="all"]')#账号
    await sel1[0].type('***',{'delay': random.randint(100, 151) - 50})
    time.sleep(1)

    sel2 = await page.xpath('//*[@id="password-number"]')#密码
    await sel2[0].type('***',{'delay': random.randint(100, 151) - 50})
    time.sleep(3)

    but2 = await page.xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/div/div[6]/div/button')
    await but2[0].click()
    time.sleep(3)

    data = await page.screenshot(path = 'D:/animation/CSDN2.png')
    # fh = open('D:/animation/CSDN2.txt', 'w', encoding='utf-8')
    # fh.write(data)
    # fh.close()
    await page.close()
asyncio.get_event_loop().run_until_complete(main())