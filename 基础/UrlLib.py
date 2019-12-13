import urllib.request
#urlretrieve(网址,本地文件存储地址) 直接下载网页到本地
#可用于将网页、网页中的图片等批量下载到本地
'''
格式：
urllib.request.urlretrieve("","")
'''

#urlcleanup() 清除相关缓存

#info() 网页的相关信息
'''
格式：
url = urllib.request.urlopen("网址")
info = url.info()
'''

#getcode()  输出网页状态码 //访问成功or失败，失败的状态码是什么（404.200这种）
'''
格式：
url = urllib.request.urlopen("网址")
code = url.getcode()
'''

#geturl()  获取当前访问的网页的url
'''
格式：
url = urllib.request.urlopen("网址")
geturl = url.geturl()
'''

