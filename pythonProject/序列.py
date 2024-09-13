#可变序列 不可变序列
#+    *
# print([1,2,3]+[4,5,6]) #[1, 2, 3, 4, 5, 6]
# print((1,2,3)+(4,5,6)) #(1, 2, 3, 4, 5, 6)
# print([1,2,3]*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# print((1,2,3)*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)
# s=[1,2,3]
# print(id(s))
# s *= 2
# print(s)
# print(id(s))
# #1.唯一标志 2. 类型 3.值
# t = (1,2,3)
# print(id(t)) #1840902520640
# t *= 2
# print(id(t)) #1840899354016
# #同一性运算符：is  is no检测对象id值是否相等
# x = "FishC"
# y = "FishC"
# print(x is y) #True
# x = [1,2,3]
# y = [1,2,3]
# print(x is y) #False
# print("鱼" in "鱼C") #True
# print("Fish" in "FishC") #True
# print("C" not in "FishC") #False
# #del 用于删除一个或多个指定对象
# x = "FishC"
# y = [1,2,3]
# del x,y
# #print(x) error
# #print(y) error
# x = [1,2,3,4,5]
# del x[1:4]
# print(x) #[1, 5]
# y = [1,2,3,4,5]
# y[1:4] = []
# print(y) #[1, 5]
# x = [1,2,3,4,5]
# del x[::2]
# print(x) #[2, 4]
# y = [1,2,3,4,5]
# #y[::2] = []
# # print(y) error
# x = [1,2,3,4,5]
# x.clear()
# print(x) #[]
# y = [1,2,3,4,5]
# del y[:]
# print(y) #[]

#相关的函数
#列表 元组 字符串相互转换函数 list(),tuple(),str()
#可迭代对象转成列表 list()
# print(list("FischC")) #['F', 'i', 's', 'c', 'h', 'C']
# print(list((1,2,3,4,5))) #[1, 2, 3, 4, 5]
# #可迭代对象转成元组 tuple()
# print(tuple([1,2,3,4,5])) #(1, 2, 3, 4, 5)
# print(tuple("FishC")) #('F', 'i', 's', 'h', 'C')
# #可迭代对象转成字符串 str()
# print(str([1,2,3,4,5])) #‘[1, 2, 3, 4, 5]'
# print(str((1,2,3,4,5))) #'(1, 2, 3, 4, 5)'
# #对比传入的参数返回最小值 最大值 min() max()
# s = [1,1,2,3,5]
# print(min(s)) #1
# t = "FishC"
# print(max(t)) #s
# s = []
# #print(min(s)) error
# print(min(s,default="pi")) #pi
# print(min(1,2,3,0,6)) #0
# print(max(1,2,3,4,5)) #5
# #len()(2的31次方-1)   sum()
# #print(len(range(2 ** 100))) #error
# s = [1,0,0,8,6]
# print(sum(s)) #15
# print(sum(s,start=100)) #115
# #sorted()   reversed()
# s = [1,2,3,0,6]
# print(sorted(s)) #[0, 1, 2, 3, 6] 列表不会被改变 输出一个新的列表
# s.sort()
# print(s) #[0, 1, 2, 3, 6]
# print(sorted(s,reverse=True)) #[6, 3, 2, 1, 0]
# t = ["FishC","Apple","Book","Banana","Pen"]
# print(sorted(t)) #['Apple', 'Banana', 'Book', 'FishC', 'Pen']
# print(sorted(t,key=len)) #['Pen', 'Book', 'FishC', 'Apple', 'Banana']
# t.sort(key=len)#sort只能处理列表
# print(t) #['Pen', 'Book', 'FishC', 'Apple', 'Banana']
# print(sorted("FishC")) #['C', 'F', 'h', 'i', 's']
# print(sorted((1,0,0,8,6))) #[0, 0, 1, 6, 8]
# #反向迭代器
# s = [1,2,5,8,0]
# print(reversed(s)) #<list_reverseiterator object at 0x000001EB72E69EA0>
# print(list(reversed(s))) #[0, 8, 5, 2, 1]
# print(list(reversed("FishC"))) #['C', 'h', 's', 'i', 'F']
# print(list(reversed((1,2,3,4,5)))) #[5, 4, 3, 2, 1]
# print(list(reversed(range(0,10)))) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#all()判断可迭代对象中是否所有元素的值都为真
# any()判断可迭代对象中是否存在元素位真
x = [1,1,0]
y = [1,1,9]
print(all(x)) #False
print(all(y)) #True
#enumerate() 用于返回一个枚举对象，将可迭代对象的每个元素及从0开始的序号共同构成一个二元组的列表
seasons = ["Spring","Summer","Fall","Winter"]
enumerate(seasons)
print(list(enumerate(seasons))) #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons,10))) #[(10, 'Spring'), (11, 'Summer'), (12, 'Fall'), (13, 'Winter')]
#zip() 用于创建一个聚合多个可迭代对象的迭代器，作为参数传入每个可迭代对象的每个元素依次组合成元组
x = [1,2,3]
y = [4,5,6]
zipper = zip(x,y)
print(list(zipper)) #[(1, 4), (2, 5), (3, 6)]
z = [7,8,9]
zipper = zip(x,y,z)
print(list(zipper)) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
z = "FishC"
zipper = zip(x,y,z)
print(list(zipper)) #[(1, 4, 'F'), (2, 5, 'i'), (3, 6, 's')]
#itertools中zip_longest()来代替zip
import itertools
zipper = itertools.zip_longest(x,y,z)
print(list(zipper)) #[(1, 4, 'F'), (2, 5, 'i'), (3, 6, 's'), (None, None, 'h'), (None, None, 'C')]
#map() 根据提供的函数对指定的可迭代对象的每个元素进行运算，并将返回运算结果的迭代器
mapped = map(ord,"FishC") #ord 将字符转成对应的编码值
print(list(mapped)) #[70, 105, 115, 104, 67]
mapped = map(pow,[2,3,10],[5,2,3])
print(list(mapped)) #[32, 9, 1000]
print(pow(2,5),pow(3,2),pow(10,3)) #32 9 1000
print(list(map(max,[1,3,5],[2,2,2],[0,3,9,8]))) #[2, 3, 9]
#filter() 根据提供的函数对指定的可迭代对象的每个元素进行运算，并将运算结果位真的元素，以迭代器的形式返回
print(list(filter(str.islower,"FishC"))) #['i', 's', 'h']
#迭代器 一个迭代器就是一个可迭代对象
#可迭代对象 可以重复使用而迭代器则是一次性的
mapped = map(ord,"FishC")
for each in mapped:
    print(each) #70 105 115 104 67
print(list(mapped)) #[]
x = [1,2,3,4,5]
y = iter(x)
print(type(x)) #<class 'list'> 列表
print(type(y)) #<class 'list_iterator'> 迭代器
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
#print(next(y)) #异常
#print(next(y)) #异常
z = iter(x)
print(next(z,"no"))
print(next(z,"no"))
print(next(z,"no"))
print(next(z,"no"))
print(next(z,"no"))
print(next(z,"no")) #no




