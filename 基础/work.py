import re
import urllib
import urllib.request
#读取出版社信息
'''
data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
print(len(data))
pat = '<div class="name">(.*?)</div>'
res = re.compile(pat).findall(data) #正则匹配
fh = open("C:/Users/asus/Desktop/text.txt","w")#追加的方式写入文件
for i in range(0,len(res)):
    try:
        fh.write(res[i]+"\n")
    except Exception in ex:
        print(ex)
fh.close()
'''

