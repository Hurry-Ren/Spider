#超时设置:设置访问时间，超时后的操作等,提高爬虫效率
import urllib
import urllib.request
try:
    fh = urllib.request.urlopen("https://www.baidu.com", timeout=1)
    print(len(fh.read().decode("utf-8")))
except Exception as err:
    print(err)