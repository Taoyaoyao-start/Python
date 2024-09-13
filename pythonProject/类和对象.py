# #对象 = 属性 + 方法
# class Turtle:
#     head = 1
#     eyes = 2
#     legs = 4
#     shell = True
#     #方法
#     def crawl(self):
#         print("11")
#     def run(self):
#         print("22")
#     def bite(self):
#         print("33")
#     def eat(self):
#         print("44")
#     def sleep(self):
#         print("55")
# t1 = Turtle()
# print(t1.head) #1
# print(t1.legs) #4
# print(t1.crawl()) #11
# print(t1.bite()) #33
# t2 = Turtle()
# print(t2.head) #1
# t2.legs = 3
# print(t2.legs) #3
# print(t1.legs) #4
# t1.mouth = 1
# print(t1.mouth)
# #封装
# x = 520
# print(type(x))
# #self
# class C:
#     def hello():
#         print("你好")
# c = C()
# #print(c.hello()) error
# class C:
#     def get_self(self):
#         print(self)
# c = C()
# print(c.get_self()) #<__main__.C object at 0x00000215EE2DE600>
# print(c) #<__main__.C object at 0x000002411A59E630>
# #传递给方法的就是实例对象本身c
#继承
# class A:
#     x = 520
#     def hello(self):
#         print("你好，我是A")
# class B(A):
#     pass
# b = B()
# print(b.x) #520
# print(b.hello()) #你好，我是A
# class B(A):
#     x = 880
#     def hello(self):
#         print("你好，我是B")
# b = B()
# print(b.x) #880
# print(b.hello()) #你好，我是B
# #isinstance 判断一个对象是否属于某个类
# print(isinstance(b,B)) #True
# print(isinstance(b,A)) #True
# #检测一个类是否是其他的字类 issubclass
# print(issubclass(A,B))#False
# print(issubclass(B,A))#True
# class B:
#     x = 880
#     y = 250
#     def hello(self):
#         print("你好，我是B")
# class C(A,B):
#     pass
# c = C()
# print(c.x) #520
# print(c.hello())  #你好，我是A
# print(c.y) #250
# #组合
# class Turtle:
#     def say(self):
#         print("11111")
# class Cat:
#     def say(self):
#         print("222")
# class Dog:
#     def say(self):
#         print("333")
# class Garden:
#     t = Turtle()
#     c = Cat()
#     d = Dog()
#     def say(self):
#         self.t.say()
#         self.c.say()
#         self.d.say()
# g = Garden()
# print(g.say()) #11111  222  333
# #绑定
# class C:
#     def get_self(self):
#         print(self)
# c = C()
# d = C()
# d.x = 250
# print(c.__dict__) #{}
# print(d.__dict__) #{'x': 250}
# d.y = 660
# print(d.__dict__) #{'x': 250, 'y': 660}
# class C:
#     def set_x(self,v):
#         self.x = v #self.x = v 相当于 c.x = v
# c = C()
# print(c.__dict__) #{}
# c.set_x(250)
# print(c.__dict__) #{'x': 250}
# print(c.x) #250
# class C:
#     x = 100
#     def set_x(self,v):
#         x = v
# c = C()
# print(c.set_x(250000))
# print(c.x) #100
# print(C.x) #100
# C.x = 250
# print(c.x) #250
# print(c.__dict__) #{}
# class C:
#     pass
# C.x = 250
# C.y = "小甲鱼"
# C.z = [1,2,3]
# print(C.x)
# print(C.y)
# print(C.z)
# d = {}
# d['x'] = 250
# d['y'] = "小甲鱼"
# d['z'] = [1,2,3]
# print(d['x'])
# print(d['y'])
# print(d['z'])
# class C:
#     pass
# c = C()
# #构造
# class C:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#     def mul(self):
#         return self.x * self.y
# c = C(2,3)
# print(c.add()) #5
# print(c.mul()) #6
# print(c.__dict__)#{'x': 2, 'y': 3}
# d = C(4,5)
# print(d.__dict__)
# #重写
# class D(C):
#     def __init__(self,x,y,z):
#         C.__init__(self,x,y)
#         self.z = z
#     def add(self):
#         return C.add(self) + self.z
#     def mul(self):
#         return C.mul(self) * self.z
# d = D(2,3,4)
# print(d.add()) #9
# print(d.mul()) #24
# class A:
#     def __init__(self):
#         print("111A")
# class B1(A):
#     def __init__(self):
#         A.__init__(self)
#         print("222B1")
# class B2(A):
#     def __init__(self):
#         A.__init__(self)
#         print("333B2")
# class C(B1,B2):
#     def __init__(self):
#         B1.__init__(self)
#         B2.__init__(self)
#         print("444C")
# c = C()
# print(c) #111A 222B1 111A 333B2 444C
# class B1(A):
#     def __init__(self):
#         super().__init__()
#         print("222B1")
# class B2(A):
#     def __init__(self):
#         super().__init__()
#         print("333B2")
# class C(B1,B2):
#     def __init__(self):
#         super().__init__()
#         print("444C")
# c = C()
# print(c) #111A 333B2 222B1 444C
# #MRO
# print(B1.mro())
# print(B2.__mro__)
# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def say(self):
#         print(f"我叫{self.name},今年{self.age}")
# class FlyMixin:
#     def fly(self):
#         print("i can fly")
# class Pig(FlyMixin,Animal):
#     def special(self):
#         print("my 技能 拱大白菜")
# p = Pig("大肠",5)
# print(p.say())
# print(p.special())
# print(p.fly())
# class Displayer:
#     def display(self,message):
#         print(message)
# class LoggerMixin:
#     def log(self,message,filename="logfile.txt"):
#         with open(filename,'a') as f:
#             f.write(message)
#     def display(self,message):
#         super().display(message)
#         self.log(message)
# class MySubClass(LoggerMixin,Displayer):
#     def log(self,message):
#         super().log(message,filename="subclasslog.txt")
# subclass = MySubClass
# print(subclass.display("This is a test."))
#多态
# print(len("FishC"))
# print(len(["Fishc","Pythn"]))
# print(len({"name":"name","age":18}))
# class Shape:
#     def __init__(self,name):
#         self.name = name
#     def area(self):
#         pass
# class Square(Shape):
#     def __init__(self,length):
#         super().__init__("正方形")
#         self.length = length
#     def area(self):
#         return self.length * self.length
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__("圆形")
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# class Triangle(Shape):
#     def __init__(self,height,base):
#         super().__init__("三角形")
#         self.base = base
#         self.height = height
#     def area(self):
#         return self.base * self.height / 2
# s = Square(5)
# c = Circle(6)
# t = Triangle(3,4)
# print(s.name) #正方形
# print(c.name) #圆形
# print(t.name) #三角形
# print(s.area()) #25
# print(c.area()) #113.03999999999999
# print(t.area()) #6.0
# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print(f"我一只猫，我叫{self.name},今年{self.age}")
#     def say(self):
#         print("mua-")
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print(f"我一只狗，我叫{self.name},今年{self.age}")
#     def say(self):
#         print("wow")
# class Pig:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print(f"我一只猪，我叫{self.name},今年{self.age}")
#     def say(self):
#         print("oink")
# c = Cat("web",4)
# d = Dog("bb",71)
# p = Pig("dac",5)
# def animal(x):
#     x.intro()
#     x.say()
# print(animal(c))
# print(animal(d))
# print(animal(p))
# #鸭子类型
# class Bicycle:
#     def intro(self):
#         print("1111")
#     def say(self):
#         print("2222")
# b = Bicycle()
# print(animal(b))
# class C:
#     def __init__(self,x):
#         self.__x = x
#     def set_x(self,x):
#         self.__x = x
#     def get_x(self):
#         print(self.__x)
# c = C(250)
# #print(c.__x)
# print(c.get_x())
# print(c.set_x(520))
# print(c.get_x())
# print(c.__dict__) #{'_C__x': 520}
# print(c._C__x) #520
# class D:
#     def __func(self):
#         print("Hello")
# d = D()
# print(d._D__func()) #Hello
# c.__y = 250
# print(c.__dict__)
# #_单个下横线开头的变量 通常内部使用
# #单下横线结尾的变量
# class C:
#     def __init__(self,x):
#         self.x = x
# c = C(250)
# print(c.x)
# print(c.__dict__)
# c.y = 520
# print(c.__dict__)
# c.__dict__['z'] = 666
# print(c.__dict__)
# print(c.z)
# #__slots__ 避免空间上的浪费
# class C:
#     __slots__ = ["x","y"]
#     def __init__(self,x):
#         self.x = x
# c = C(250)
# print(c.x)
# c.y = 520
# print(c.y)
# #c.z = 666 error
# class D:
#     __slots__ = ["x","y"]
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
# #d = D(3,4,5) error
# #继承自父类的__slots__属性是不会在字类中生效的
# class E(C):
#     pass
# e = E(250)
# print(e.x)
# e.y = 520
# print(c.y)
# e.z = 666
# print(e.__slots__) #['x', 'y']
# print(e.__dict__) #{'z': 666}
# class CapStr(str):
#     def __new__(cls, string):
#         string = string.upper()
#         return super().__new__(cls,string)
# cs = CapStr("FishC")
# print(cs) #CapStr继承自str类
# print(cs.lower())
# print(cs.capitalize())
# class C:
#     def __init__(self):
#         print("111")
#     def __del__(self):#对象销毁时调用
#         print("222")
# c = C()
# del c
# c = C()
# d = c #111
# del c
# del d #222
# class D:
#     def __init__(self,name):
#         self.name = name
#     def __del__(self):
#         global x
#         x = self
# d = D("111")
# print(d) #<__main__.D object at 0x000001872E3CDD60>
# del d
# print(x) #<__main__.D object at 0x0000026EFEADDD30>
# class E:
#     def __init__(self,name,func):
#         self.name = name
#         self.func = func
#     def __del__(self):
#         self.func(self)
# def outter():
#      x = 0
#      def inner(y = None):
#          nonlocal x
#          if y:
#              x = y
#          else:
#              return x
#      return inner
# f = outter()
# e = E("111",f)
# print(e)
# print(e.name)
# del e
# g = f()
# print(g)
# class S(str):
#     def __add__(self, other):
#         return len(self) + len(other )
# s1 = S("FishC")
# s2 = S("Python")
# print(s1 + s2)
# print(s1 + "Python")
# print("Fishc"+ s2)
# class S1(str):
#     def __add__(self, other):
#         return NotImplemented
# class S2(str):
#     def __radd__(self, other):
#         return len(self) + len(other)
# s1 = S1("Apple")
# s2 = S2("Banana")
# print(s1 + s2)
# class S1(str):
#     def __iadd__(self, other):
#         return len(self) + len(other)
# s1 = S1("Apple")
# s1 += s2
# print(s1)
# print(type(s1))
# s2 += s2
# print(s2)
# print(type(s2))
# print(3 & 2)
# print(3 & 4)
# print(bin(3))
# print(bin(4))
# print(3 | 2)
# print(3 | 4)
# print(~2)
# print(~4)
# print(~3)
# print(3 ^ 2)
# print(3 ^ 4)
# print(8 >> 2)
# print(8 >> 3)
# print(8 << 2)
# print(8 // pow(2,2))
# print(9 >> 2)
# import math
# print(0.1 + 0.2 == 0.3 + math.ulp(0.3))
# class C:
#     def __index__(self):
#         print("被拦截了-")
#         return 3
# c = C()
# #print(c[2]) error
# s = "FishC"
# print(s[c])
# print(bin(c))
# class C:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
# c = C("小甲鱼",18)
# print(hasattr(c,"name")) #检测是否有这个属性
# print(getattr(c,"name")) #获取对象中某个属性值
# print(getattr(c,"_C__age"))
# setattr(c,"_C__age",19)
# print(getattr(c,"_C__age"))
# print(delattr(c,"_C__age"))
# print(hasattr(c,"_C__age"))
# class C:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def __getattribute__(self, attrname):
#         print("拿来吧你")
#         return super().__getattribute__(attrname)
# c = C("小甲鱼",18)
# print(getattr(c,"name")) #拿来吧你 小甲鱼
# print(c._C__age) #拿来吧你 18
# class C:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def __getattribute__(self, attrname):
#         print("拿来吧你")
#         return super().__getattribute__(attrname)
#     def __getattr__(self, attrname):
#         if attrname == "FishC":
#             print("I love FishC")
#         else:
#             raise AttributeError(attrname)
# c = C("小甲鱼",18)
# print(c.FishC)
# #print(c.x)
# class D:
#     def __setattr__(self, name, value):
#         self.name = value
# d = D()
# #d.name = "小甲鱼" error
# class D:
#     def __setattr__(self, name, value):
#         self.__dict__[name] = value
# d = D()
# d.name = "小甲鱼"
# print(d.name)
# class D:
#     def __setattr__(self, name, value):
#         self.__dict__[name] = value
#     def __delattr__(self, name):
#         del self.__dict__[name]
# d = D()
# d.name = "小甲鱼"
# print(d.__dict__)
# del d.name
# print(d.__dict__)
# class C:
#     def __getitem__(self, index):
#         print(index)
# c = C()
# print(c[2])
# print(c[2:8])
# s = "I love FishC"
# print(s[2:6])
# print(s[slice(2,6)])
# print(s[7:])
# print(s[slice(7,None)])
# print(s[::4])
# print(s[slice(None,None,4)])
# class D:
#     def __init__(self,data):
#         self.data = data
#     def __getitem__(self, index):
#         return self.data[index]
#     def __setitem__(self, index, value):
#         self.data[index] = value
# d = D([1,2,3,4,5])
# print(d[1])
# d[1] = 1
# print(d[1])
# print(d[2:4])
# print(d[:])
# class D:
#     def __init__(self,data):
#         self.data = data
#     def __getitem__(self, index):
#         return self.data[index] * 2
# d = D([1,2,3,4,5])
# for i in d:
#     print(i,end=' ')
# x = [1,1,2,3,5]
# for i in x:
#     print(i,end=' ')
# _ = iter(x)
# while True:
#     try:
#         i = _.__next__()
#     except StopIteration:
#         break
#     print(i,end=' ')
# class Double:
#     def __init__(self,start,stop):
#         self.value = start - 1
#         self.stop = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value * 2
# d = Double(1,5)
# for i in d:
#     print(i,end=' ')
# class C:
#     def __init__(self,data):
#         self.data = data
#     def __contains__(self, item):
#         print("嗨")
#         return item in self.data
# c = C([1,2,3,4,5])
# print(3 in c)
# print(6 in c)
# class C:
#     def __init__(self,data):
#         self.data = data
#     def __iter__(self):
#         print("Iter",end = ' ->')
#         self.i = 0
#         return self
#     def __next__(self):
#         print("Next",end=' -> ')
#         if self.i == len(self.data):
#             raise StopIteration
#         item = self.data[self.i]
#         self.i += 1
#         return item
# c = C([1,2,3,4,5])
# print(3 in c)
# print(6 in c)
# class C:
#     def __init__(self,data):
#         self.data = data
#     def __getitem__(self, index):
#         print("Getitem",end = ' - > ')
#         return self.data[index]
# c = C([1,2,3,4,5])
# print(3 in c)
# print(6 in c)
# class D:
#     def __bool__(self):
#         print("Bool")
#         return True
# d = D()
# print(bool(d))
# class D:
#     def __init__(self,data):
#         self.data = data
#     def __len__(self):
#         print("len")
#         return len(self.data)
# d = D("FishC")
# print(bool(d))
# d = D("")
# print(bool(d))
# class S(str):
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __gt__(self, other):
#         return len(self) > len(other)
#     def __eq__(self, other):
#         return len(self) == len(other)
# s1 = S("FishC")
# s2 = S("fishc")
# print(s1 < s2)
# print(s1 > s2)
# print(s1 == s2)
# print(s1 != s2)
# print(s1 <= s2)
# class S(str):
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __gt__(self, other):
#         return len(self) > len(other)
#     def __eq__(self, other):
#         return len(self) == len(other)
#     __le__ = None
#     __ge__ = None
#     __ne__ = None
# s1 = S("FishC")
# s2 = S("fishc")
# #print(s1 != s2) error
# class C:
#     def __init__(self,data):
#         self.data = data
#     def __iter__(self):
#         print("Iter",end = ' ->')
#         self.i = 0
#         return self
#     def __next__(self):
#         print("Next",end=' -> ')
#         if self.i == len(self.data):
#             raise StopIteration
#         item = self.data[self.i]
#         self.i += 1
#         return item
#     __contains__ = None
# c = C([1,2,3,4,5])
# #print(3 in c) error
# class C:
#     def __call__(self, *args, **kwargs):
#         print(f"位置参数->{args}\n关键字参数->{kwargs}")
# c = C()
# c(1,2,3,x=250,y = 520)
# class Power:
#     def __init__(self,exp):
#         self.exp = exp
#     def __call__(self, base):
#         return base ** self.exp
# square = Power(2)
# print(square(2))
# print(square(5))
# cube = Power(3)
# print(cube(2))
# class C:
#     def __repr__(self):
#         return "I love FishC"
# c = C()
# print(repr(c))
# print(str(c))
# class C:
#     def __str__(self):
#         return "I love FishC"
# c = C()
# print(str(c))
# print(repr(c))
# cs = [C(),C(),C()]
# for each in cs:
#     print(each)
# print(cs)
# class C:
#     def __repr__(self):
#         return "I LOVE FihsC"
# cs = [C(),C(),C()]
# for each in cs:
#     print(each)
# print(cs)
# class C:
#     def __init__(self,data):
#         self.data = data
#     def __str__(self):
#         return f"data = {self.data}"
#     def __repr__(self):
#         return f"C({self.data})"
#     def __add__(self, other):
#         self.data += other
# c = C(250)
# print(c)
# c
# c + 250
# print(c)
# c








