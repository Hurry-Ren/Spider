#文件的操作
#打开     open(文件地址,操作形式)     w:写入    r:读取    b:二进制   a:追加
fh = open("C:/Users/asus/Desktop/text.txt","r")

#读取     read()读取全部   readline(x)读取某行
data = fh.read()
line = fh.readline()
fh.close()
#关闭文件  fh.close()

#文件的写入
data = "学好Python"
fh = open("C:/Users/asus/Desktop/text.txt","w")     #w 写入可能会覆盖   a/a+ 追加
fh.write(data)
fh.close()