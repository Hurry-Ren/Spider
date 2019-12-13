from 基础.ua_ip import *
import urllib.request

keyword = "兰博基尼"
key = urllib.request.quote(keyword)
pat = ' data-lazy-img="//img(.*?).360buyimg.com/n9/jfs/(.*?).jpg"'

for i in range(1,11):
    url = "https://search.jd.com/Search?keyword="+str(key)+"&enc=utf-8&page="+str((i*2)-1)
    print(url)
    try:
        results = ua_ip(url, pat)
        for j in range(0, len(results)):
            thisurl = "http://img" + results[j][0] + ".360buyimg.com/n1/jfs/" + results[j][1] + ".jpg"
            file = "C:/Users/asus/Desktop/data/JD/" + str(i) + "_" + str(j) + ".jpg"
            urllib.request.urlretrieve(thisurl, filename=file)
    except Exception as err:
        if hasattr(err,"code"):
            print(err.code)
        if hasattr(err,"reason"):
            print(err.reason)