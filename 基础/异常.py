#异常处理
'''
try:
    程序
except Exception as 异常名:    #这里是获取异常的名字，可根据不同异常进行不同处理
    异常处理部分
'''

#URLError和HTTPError
#URLError是母类，无异常状态码
#HTTPError是子类，有异常状态码与异常原因
'''
URLError出现原因：
1）连不上服务器
2）远程url不存在
3）无网络
4）处罚HTTPError
'''

import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://bolg.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)

