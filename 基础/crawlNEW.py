import urllib.request
import re

def __xunhuan__(url,headers):
    req = urllib.request.Request(url)
    req.add_header = headers
    data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
    #data = opener.open(url,timeout=1).read().decode("utf-8","ignore")
    print(len(data))
    target = '<h2>(\s*?)<a href="(.*?)"'
    rst = re.compile(target).findall(data)
    print(rst[1][1])
    for i in range(len(rst)):
        try:
            urllib.request.urlretrieve( rst[i][1], "C:/Users/asus/Desktop/data/" + str(i) + ".html")
            print(rst[i][1])
            __xunhuan__(rst[i],headers) #因为blog网页下面的博文源码形式不一样，所以需要进行判断，可能太多会卡死
        except urllib.error.URLError as err:
            if hasattr(err, "code"):
                print(err.code)
            if hasattr(err, "reason"):
                print(err.reason)


url = "https://blog.csdn.net/"
headers=("User_Agent"," Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


opener = urllib.request.build_opener()
opener.addheaders = [headers]
#安装为全局
urllib.request.install_opener(opener)
#data = opener.open(url).read().decode("utf-8","ignore")

__xunhuan__(url,headers)



