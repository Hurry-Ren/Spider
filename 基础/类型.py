'''
数、字符串、列表、元组、集合、字典
'''
a1 = 1
a2 = "hij"
a3 = 'opq'

# 列表：存储多个元素的东西，列表里面的元素是可以重新赋值的
b = [7, "cd", 'de', 60]
print(b[1])

# 元组：存储多个元素的东西，元组里面的元素是不可以重新赋值的
c = ("cd", 'de', 60)
print(c)

# 字典 {键：值，...}
# 取值格式：字典名["对应键名"]
d = {"name": "RYY", "sex": "男"}
print(d["name"])

# 集合  作用：去重
e = set("abccbd")
f = set("bcd")
g = e - f
h = e and f
print(e)
# e,f的差集
print(g)
# e,f的并集
print(h)

#   + 可用于字符串链接

# if
'''
    if():
    elif():
    elif():
    else:
'''

# while
'''
a=10
while(a<10):
    print(a)
    a++
'''

# for
'''
遍历数组：
a=["abn",7,6]
for i in a:
    print(i)
'''
'''
循环：
for i in range(0,10)//输出0-9
'''
# end()不换行   str()转换成字符  range(10,0,-1)输出9到0

for i in range(9, 1, -1):
    for j in range(9, 1, -1):
        if (i > j):
            break
        print(str(i) + "*" + str(j) + "=" + str(i * j), end=("\t"))
    print()
