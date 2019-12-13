#继承：把一个或多个类（基类）的特征拿过来
#重载：在子特征重新定义类（派生类）里面对继承过来的
#父类:基类
#子类：派生类

class father:
    def speak(self):
        print("说话")

class son(father):#单继承
    pass

class mother:
    def write(self):
        print("写字")

class daughter(father,mother):#多继承
    def read(self):
        print("读")
a = daughter()
a.read()
a.write()
a.speak()