# -*- coding: utf-8 -*-

#要求：登陆CSDN，并访问其他深层网页
#难点：表单数据的提交，cookie

import scrapy
from scrapy.http import Request,FormRequest
from CSDN.items import CsdnItem
                                            #这个爬虫没写出来，留着后期解决
class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://csdn.net/']
    header = {"User_Agent":"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"}

    #编写start_requests，第一次默认调用该方法。若没有则调用上面的start_urls
    def start_requests(self):
        #首先爬一次登录页，然后进入回调函数parse()
        return  [Request(url = "https://passport.csdn.net/login?code=public",
                         meta = {"cookiejar":1},
                         callback = self.parse)
                 ]

    def parse(self, response):
        #设置传递的post信息
        #print(response.body)
        data = {
            #"loginType":"1",
            "pwdOrVerifyCode":"",
            "userIdentification":"",
            #"uaToken":"120"
        }
        print("正在登录。。。")

        #通过FormRequest.from_response()进行登陆
        #"https://passport.csdn.net/v1/register/pc/login/doLogin"
        return FormRequest(url="https://passport.csdn.net/v1/register/pc/login/doLogin",
                           # 访问方式
                           method="POST",
                           # 设置cookie信息
                           meta={"cookiejar": response.meta["cookiejar"]},
                           # 设置header信息模拟成浏览器
                           # header = self.header,
                           # 设置post表单中的数据
                           formdata=data,
                           # 不进行去重处理
                           dont_filter=True,
                           # 设置回调函数，此时是回调函数next()
                           callback=self.next1,
        )

    def next1(self,response):
        print("已登录成功")
        #response.body是响应中的全部数据
        a= response.xpath("/html/haed/title/text()").extract()
        print(a)
        yield Request("https://i.csdn.net/#/uc/profile",
                      callback=self.next2,
                      meta={"cookiejar": 1}
                      )

    def next2(self,response):
        print("已进入个人中心")
        b = response.xpatn("/html/haed/title/text()").extract()
        print(b)
