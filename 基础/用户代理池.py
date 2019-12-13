import urllib.request
import re
import random

uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0) QQBrowser/6.0"
]

def ua(uapools):
    thisua = random.choice(uapools)#选择代理
    print(thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = ["User_Agent",thisua]
    #安装为全局
    urllib.request.install_opener(opener)

def work():
    pass
    #这里进行相应的爬去操作