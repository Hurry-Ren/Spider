import urllib.request
import re
#伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
'''
#get请求:  .html?字段=值&字段=值...
keyword = "成龙"
#若keyword是中文,需要转码 ：
keyword = urllib.request.quote(keyword)
#pn 页数
for i in range(1,2):#1-10页
    chaper_url = "https://www.bilibili.com/video/av56504908/?p=" + str(i)
    req = urllib.request.Request(url=chaper_url, headers=headers)
    url = urllib.request.urlopen(req).read().decode("utf-8")
    print(url.geturl())
    print(len(url))
    key = '"part":"(.*?)"'
    rst = re.compile(key).findall(url)
    print(rst)
'''
#post提交
import urllib.request
import urllib.parse

posturl = "http://www.iqianyue.com/mypost"
postdata = urllib.parse.urlencode({
    "name":"RYYyyyyyy",
    "pass":"RYYyyyyyyy",
}).encode("utf-8")
#进行post就需要使用urllib.requset下面的Request(真实地址，post的数据)
req = urllib.request.Request(posturl,postdata)
rst = urllib.request.urlopen(req).read().decode("utf-8")
fh = open("C:/Users/asus/Desktop/post.html","w")
fh.write(rst)
fh.close()
