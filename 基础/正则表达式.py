import re
import urllib.request

string = '''huadongjiaotongdaxue
            ligongxueyuan
        '''
#普通字符作为原子
pat = "da"
rst = re.search(pat,string)
print(rst)

#非打印字符做原子   \n换行符  \t制表符
pat = "\n"
rst = re.search(pat,string)
print(rst)

#通用字符作为原子
'''
\w 匹配任意一个字母、数字、下划线
\W 匹配除字母、数字、下划线
\d 匹配十进制数
\D 匹配除十进制数外任意一个字符
\s 匹配空白字符
\S 匹配除空白字符外任意字符
'''

string = "huadong126i98 kj84"
pat = "\w\d\d\s\w"
rst = re.search(pat,string)
print(rst)

#原子表    [xyz]:xyz任意选择中一个 ^xyz除xyz其他字符(^是非的意思)
pat = "hua[^d]"
rst = re.search(pat,string)
print(rst)

#元字符：正则表达式中具有一些特殊含义的字符，比如重复N次前面的字符等
'''
. :除换行符以外的任意一个字符
^ :匹配开始的位置
$ :匹配结束的位置
* :前面的字符重复出现0、1、多次
? :前面的字符重复出现0、1
+ :前面的字符重复出现1、多次
{n} :前面的字符恰好出现n次
{n,} :前面的字符至少出现n次
{n,m} :前面的字符至少出现n次，至多m次
| ：模式选择符或
() :模式单元
'''
string = "huadong126i98 kj84"
pat1 = "hua.*"
rst = re.search(pat,string)
print(rst)

#模式修正符：可以在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能
'''
I 匹配是忽略大小写
M 多行匹配*
L 本地化识别匹配
U unicode
S 让.匹配换行符
'''
string = "Python"
pat = "pyt"
rst = re.search(pat,string,re.I)
print(rst)

#贪婪模式；尽可能多的匹配
#懒惰模式：尽可能少的匹配
string = "poythony"
pat1 = "p.*y"    #默认为贪婪模式
pat2 = "p.*?y"   #加了？变成了懒惰模式，相对精准
rst1 = re.search(pat1,string,re.I)
rst2 = re.search(pat2,string,re.I)
print(rst1)
print(rst2)

#正则表达式函数 ：re.match()、re.search()、全局匹配函数、re.sub()函数
#match() 只能从头开始匹配
#search() 可以任意地方开始匹配
#全局匹配 格式：re.compile(正则表达式).findall(数据)
string1 = "sdspoytphony"
pat1 = "p.*?y"
rst1 = re.compile(pat1).findall(string1)
print(rst1)


#实例：匹配.com和.cn
string = "<a href='https://www.baidu.com/read/pages'>"
pat = "[a-zA-Z]+://[^\s]*[.com|.cn]"
rst = re.compile(pat).findall(string)
print(rst)

#实例：匹配电话号码
string = "<a href='ht0797-1324515tps://www.baidu.com321-13245515tps://www.ba'>"
pat = "\d{4}-\d{7}|\d{3}-\d{8}"
rst = re.compile(pat).findall(string)
print(rst)

#简单爬虫
string = urllib.request.urlopen("https://www.bilibili.com").read().decode('utf-8')
pat = "[a-zA-Z]+://[^\s]*[.com|.cn]"
rst = re.compile(pat).findall(string)
print(rst)


