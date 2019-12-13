#浏览器伪装
#头文件格式  headers=("User_Agent",具体用户代码值)

import urllib.request

url = "http://blog.csdn.net"
headers=("User_Agent"," Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
data = opener.open(url).read()
print(len(data))
fh = open("C:/Users/asus/Desktop/post.html","wb")
fh.write(data)
fh.close()

'''
问题：
1.如何将opener安装为全局，让urlopen()访问时也添加报头？
    答：
2.研究使用Request的方式进行报头添加urllib？
    答：request.Request()中的add_header()
'''

