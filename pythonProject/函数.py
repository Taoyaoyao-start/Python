# #创建和调用函数
# def myfunc():
#     pass
# def myfunc():
#     for i in range(3):
#         print("I love FishC.")
# print(myfunc())
# #函数的参数
# def myfunc(name):
#     for i in range(3):
#         print(f"I love {name}")
# print(myfunc("Python"))
# def myfunc(name,times):
#     for i in range(times):
#         print(f"I love {name}.")
# print(myfunc("Python",5))
#
# def div(x,y):
#     z = x/y
#     return z
# print(div(4,2)) #2.0
# def div(x,y):
#     if y == 0:
#         return "除数不能为0！"
#     else:
#         return x/y
# print(div(4,0)) #除数不能为0！
# def div(x,y):
#     if y == 0:
#         return "除数不能为0！"
#     return x/y
# print(div(4,0)) #除数不能为0！

# def myfunc(s,vt,o):
#     return "".join((o,vt,s))
# print(myfunc("小甲鱼","打了","我")) #我打了小甲鱼
# #关键字参数
# print(myfunc(o="我",vt="打了",s="小甲鱼")) #我打了小甲鱼
# #默认参数
# def myfunc(s,vt,o="小甲鱼"):
#     return "".join((o,vt,s))
# print(myfunc("香蕉","吃")) #小甲鱼吃香蕉
# #def myfunc(s="苹果",vt,o = "小甲鱼") error 默认参数需要放在后面
#     #return "".join((o,vt,s))
# def myfunc(vt,s="苹果",o="小甲鱼"):
#     return "".join((o,vt,s))
# print(myfunc("拱了")) #小甲鱼拱了苹果
# print(help(abs)) #查看函数文档 abs(x, /)
# print(help(sum)) #sum(iterable, /, start=0)
# #斜杠左侧参数必须传递位置参数而不能是关键字参数
# print(abs(-1.5))
# #print(abs(x=-1.5)) #error
# print(sum([1,2,3],4))
# print(sum([1,2,3],start=4))
# def abc(a,/,b,c):
#     print(a,b,c)
# print(abc(1,2,3))
# #print(abc(a=1,2,3)) #error
# print(abc(3,b=2,c=1))
# #*左侧随意 右侧只能是关键字参数
# def abc(a,*,b,c):
#     print(a,b,c)
# #print(abc(1,2,3)) #error
# print(abc(1,b=2,c=3))
# print(abc(a=1,b=2,c=3))

#收集参数 将元素打包成元组
# def myfunc(*args):
#     print("有{}个参数".format(len(args)))
#     print("第二个参数是：{}".format(args[1]))
# print(myfunc("小甲鱼","不二如是")) #有2个参数 第二个参数是：不二如是
# print(myfunc(1,2,3,4,5)) #有5个参数  第二个参数是：2
# def myfunc(*args):
#     print(args)
# print(myfunc(1,2,3,4,5)) #(1, 2, 3, 4, 5)
# def myfunc():
#     return 1,2,3
# print(myfunc()) #(1, 2, 3)
# x,y,z = myfunc()
# print(x,y,z) #1 2 3
# def myfunc(*args):
#     print(type(args))
# print(myfunc(1,2,3,4,5)) #<class 'tuple'>
# def myfunc(*args,a,b):
#     print(args,a,b)
# #print(myfunc(1,2,3,4,5)) #error
# print(myfunc(1,2,3,a=4,b=5)) #(1, 2, 3) 4 5
# #打包成字典 使用两个连续得**
# def myfunc(**kwargs):
#     print(kwargs)
# print(myfunc(a=1,b=2,c=3)) #{'a': 1, 'b': 2, 'c': 3}
# def myfunc(a,*b,**c):
#     print(a,b,c)
# print(myfunc(1,2,3,4,x=5,y=6)) #1 (2, 3, 4) {'x': 5, 'y': 6}
# #format 同时拥有两个参数：元组 字典
# #解包参数
# args = (1,2,3,4)
# def myfunc(a,b,c,d):
#     print(a,b,c,d)
# #print(myfunc(args)) #error
# print(myfunc(*args)) #1 2 3 4
# kwargs = {'a':1,'b':2,'c':3,'d':4}
# print(myfunc(**kwargs)) #1 2 3 4
#作用域
#局部作用域
# def myfunc():
#     x = 520
#     print(x)
# print(myfunc()) #520
# #print(x) #error
# #全局作用域
# x = 880
# def myfunc():
#     print(x)
# print(myfunc()) #880
# def myfunc():
#     x = 520
#     print(x)
# print(myfunc()) #520
# print(x) #880
# print(id(x)) #2616193057072
# def myfunc():
#     print(id(x))
# print(myfunc()) #2616193057072
# def myfunc():
#     x = 520
#     print(id(x))
# print(myfunc()) #2616190212400
# #global语句 修改全局变量
# x = 880
# def myfunc():
#     global x
#     x = 520
#     print(x)
# print(myfunc()) #520
# print(x) #520
# #嵌套函数
# def funA():
#     x = 520
#     def funB():
#         x = 880
#         print("In funB,x = ",x)
#     funB()
#     print("In FunA,x=",x)
# print(funA()) #In funB,x =  880 In FunA,x= 520
# #nonlocal语句 可以实现僭越
# def funA():
#     x = 520
#     def funB():
#         nonlocal x
#         x = 880
#         print("In funB,x = ",x)
#     funB()
#     print("In FunA,x=",x)
# print(funA()) #In funB,x =  880 In FunA,x= 880
# #LEGB 解析机制 local局部作用域 enclosed嵌套函数的外层函数作用域 global全局作用域 build内置作用域
# str = "小甲鱼把str给毁了"
# #str(520) error
#闭包 工厂函数
# def myfunc():
#     x = 520
#     print(x)
# print(myfunc())
# #print(x) #error
# def funA():
#     x = 880
#     def funB():
#         print(x)
#     return funB
# print(funA()) #<function funA.<locals>.funB at 0x000002086F00AFC0>
# print(funA()()) #880
# funny = funA()
# print(funny()) #880
# def power(exp):
#     def exp_of(base):
#         return base ** exp
#     return exp_of
# square = power(2)
# cube = power(3)
# print(square(2)) #4
# print(square(5)) #25
# print(cube(2)) #8
# print(cube(5)) #125
# def outer():
#     x = 0
#     y = 0
#     def inner(x1,y1):
#         nonlocal x,y
#         x += x1
#         y += y1
#         print(f"现在，x = {x},y = {y}")
#     return inner
# move = outer()
# print(move(1,2)) #现在，x = 1,y = 2
# print(move(-2,2)) #现在，x = -1,y = 4
# #角色移动
# origin = (0,0)
# legal_x = [-100,100]
# legal_y = [-100,100]
# def create(pos_x=0,pos_y=0):
#     def moving(direction,step):
#         nonlocal pos_x,pos_y
#         new_x = pos_x + direction[0]*step
#         new_y = pos_y + direction[1]*step
#
#         if new_x < legal_x[0]:
#             pos_x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             pos_x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             pos_x = new_x
#         if new_y < legal_y[0]:
#             pos_y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             pos_y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             pos_y = new_y
#         return pos_x,pos_y
#     return moving
# move = create()
# print("向右移动20步后，位置是：",move([1,0],20)) #向右移动20步后，位置是： (20, 0)
# print("向上移动120步后，位置是：",move([0,1],120)) #向上移动120步后，位置是： (20, 80)
# print("向右下角移动88步后，位置是：",move([1,-1],88)) #向右下角移动88步后，位置是： (92, -8)
# def myfunc():
#     print("正在调用myfunc。。。")
# def report(func):
#     print("主任，我要开始调用函数了。。。")
#     func()
#     print("主人，我调用完函数了")
# print(report(myfunc))
import time
# def time_master(func):
#     print("开始运行程序。。。")
#     stat = time.time()
#     func()
#     stop = time.time()
#     print("结束程序运行。。")
#     print(f"一共耗费了{(stop-stat):.2f}秒。")
# def myfunc():
#     time.sleep(2)
#     print("Hello FishC。")
# print(time_master(myfunc))
#装饰器 @函数
# def time_master(func):
#     def call_func():
#         print("开始运行程序。。。")
#         stat = time.time()
#         func()
#         stop = time.time()
#         print("结束程序运行。。")
#         print(f"一共耗费了{(stop-stat):.2f}秒。")
#     return call_func
# #语法糖
# @time_master
# def myfunc():
#     time.sleep(2)
#     print("Hello FishC。")
# #myfunc = time_master(myfunc)
# print(myfunc())
#多个装饰器用在一个函数上
# def add(func):
#     def inner():
#         x = func()
#         return x+1
#     return inner
# def cube(func):
#     def inner():
#         x = func()
#         return x*x*x
#     return inner
# def square(func):
#     def inner():
#         x = func()
#         return x*x
#     return inner
# @add
# @cube
# @square
# def test():
#     return 2
# print(test()) #先square 再cube 再add
# #如何给装饰器传递参数
# import time
# def logger(msg):
#     def time_master(func):
#         def call_func():
#             start = time.time()
#             func()
#             stop = time.time()
#             print(f"[{msg}]一共耗费了{(stop-start):.2f}")
#         return call_func
#     return time_master
# @logger(msg="A") #funA = logger(msg='A')(funA)
# def funA():
#     time.sleep(1)
#     print("正在调用FUNA。。。")
# @logger(msg="B")
# def funB():
#     time.sleep(1)
#     print("正在调用funB。。。")
# print(funA())
# print(funB())
#lambda 匿名函数
# squareY = lambda y:y*y
# print(squareY(3)) #9
# print(squareY) #<function <lambda> at 0x000001AD714A5440>
# y = [lambda x : x * x,2,3]
# print(y[0](y[1]))#4
# print(y[0](y[2])) #9
# mapped = map(lambda x:ord(x)+10,"FishC")
# print(list(mapped)) #[80, 115, 125, 114, 77]
# def boring(x):
#     return ord(x) + 10
# print(list(map(boring,"FishC"))) #[80, 115, 125, 114, 77]
# print(list(filter(lambda x :x%2,range(10)))) #[1, 3, 5, 7, 9]
#生成器
# def counter():
#     i = 0
#     while i <= 5:
#         yield i
#         i += 1
# print(counter()) #<generator object counter at 0x0000019B028C4E80>
# for i  in counter():
#     print(i)
# c = counter()
# print(c)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# #print(next(c)) error
# c = counter()
# #c[2] error
# def fib():
#     back1,back2 = 0,1
#     while True:
#         yield back1
#         back1,back2 = back2,back1+back2
# f = fib()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# #生成器表达式
# t = (i ** 2 for i in range(10))
# print(next(t))
# print(next(t))
# print(next(t))
# for i in t:
#     print(i)
#递归
# def funA():
#     print("AWBDYL")
# def funB():
#     funA()
# print(funB())
# def funC():
#     print("AWBDYL")
#     funC()
# #print(funC())
# def funC(i):
#     if i > 0:
#         print("AWBDYL")
#         i -= 1
#         funC(i)
# print(funC(10))
# def factIter(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
# print(factIter(5)) #120
# def factRecur(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factIter(n-1)
# print(factRecur(5)) #120
# def fibUter(n):
#     a = 1
#     b = 1
#     c = 1
#     while n > 2:
#         c = a + b
#         a = b
#         b = c
#         n -= 1
#     return c
# print(fibUter(12))
# def fibIter(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return factIter(n-1) + factIter(n-2)
# print(fibIter(12))
#汉诺塔
# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x,'--->',z)
#     else:
#         hanoi(n-1,x,z,y)
#         print(x,'--->',z)
#         hanoi(n-1,y,x,z)
# n = int(input('请输入汉诺塔的层数：'))
# hanoi(n,'A','B','C')
#函数文档 help
# print(help(print))
# def exchange(dollar,rate = 6.32):
#     """
#     功能：汇率转换，美元 -> 人民币
#     参数：-dollar 美元数量 -rate 汇率，默认值是6.32（2022-03-08）
#     返回值：人民币的数量
#     """
#     return dollar * rate
# print(exchange(20)) #126.4
# print(help(exchange))
#
# #类型注释
# def times(s:str,n:int) -> str:
#     return s*n
# print(times("FishC",5)) #FishCFishCFishCFishCFishC
# def times(s:str = "FishC",n:int = 3) -> str:
#     return s*n
# print(times()) #FishCFishCFishC
# def times(s:list,n:int = 3) -> list:
#     return s*n
# print(times([1,2,3])) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# def times(s:list[int],n:int = 3) -> list:
#     return s*n
# def times(s:dict[str,int],n:int = 3) -> list:
#     return list(s.keys()) * n
# print(times({'A':1,'B':2,'C':3})) #['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
# #内省 name annotation
# print(times.__name__) #times
# print(times.__annotations__) #{'s': dict[str, int], 'n': <class 'int'>, 'return': <class 'list'>}
# print(exchange.__doc__)
#高阶函数 functools  partial偏函数
#reduce
def add(x,y):
    return x + y
import functools
print(functools.reduce(add,[1,2,3,4,5])) #add(add(add(add(1,2),3),4),5)
print(functools.reduce(lambda x,y:x*y,range(1,11)))
square = functools.partial(pow,exp = 2)
print(square(2))
print(square(3))
cub = functools.partial(pow,exp = 3)
print(cub(2))
print(cub(3))
#@wraps 装饰器









