#IP代理：使爬虫用代理IP去爬去对方网站(数量少，容易失效，尽量使用外国ip，国内失效率高)
#IP代理的构建：
import urllib.request
import random

ip = "125.120.201.120:808"
proxy = urllib.request.ProxyHandler({"http":ip})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url = ""
data1 = urllib.request.urlopen(url).read()
data = data1.decode("utf-8")#分开写

#ip代理池
#第一种方案：（适合于代理IP稳定的情况）
ippools = [
    "",
    "",
    ""
]
def ipproxy(ippools):
    ip = random.choice(ippools)
    proxy = urllib.request.ProxyHandler({"http":ip})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

#第二种方案：（接口调用方式，适合代理IP不稳定）
import urllib.request
import random
def ipproxy():
    ip = urllib.request.urlopen("接口文档内对网址的拼接").read().decode("utf-8")
    proxy = urllib.request.ProxyHandler({"http":ip})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
