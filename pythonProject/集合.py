# print(type({})) #<class 'dict'>
# print(type({"one"})) #<class 'set'>
# print(type({"one":1})) #<class 'dict'>
# #集合中所有元素都应该是独一无二的并且也是无序的
# print({"FishC","Python"}) #{'FishC', 'Python'}
# print({s for s in "FishC"}) #{'F', 'i', 's', 'C', 'h'}
# print(set("FishC")) #{'C', 'F', 's', 'h', 'i'}
# s = set("FishC")
# #s[0] error
# print('C' in s) #True
# print('c' not in s) #True
# for each in s:
#     print(each) #C h i s F
# print(set([1,1,2,3,5])) #{1, 2, 3, 5}
# s = [1,1,2,3,5]
# print(len(s) == len(set(s))) #False
#
# #浅拷贝 copy
# t = s.copy()
# print(t) #[1, 1, 2, 3, 5]
# s = set("FishC")
# print(s) #{'F', 'i', 'C', 's', 'h'}
# #isdisjoint() 判断两个集合是否无交集
# print(s.isdisjoint(set("Python"))) #False
# print(s.isdisjoint(set("Java"))) #True
# print(s.isdisjoint("Java")) #True
# print(s.isdisjoint("Python")) #False
# #issubset 检测一个集合是否是另外一个集合的子集
# print(s.issubset("FishC.com.cn")) #True
# #issuperset 检测是否另外一个集合的超集
# print(s.issuperset("Fish")) #True
# #检测当前集合与其他集合共同构建的并集，交集，差集，以及对称差集
# #union 并集
# print(s.union({1,2,3})) #{1, 2, 's', 3, 'h', 'C', 'F', 'i'}
# #intersection 交集
# print(s.intersection("Fish")) #{'s', 'F', 'h', 'i'}
# #difference 差集
# print(s.difference("Fish")) #{'C'}
# print(s.union({1,2,3},"Python")) #{1, 2, 3, 'P', 't', 'y', 'n', 'F', 'C', 'h', 'i', 's', 'o'}
# print(s.intersection("Php","Python")) #{'h'}
# print(s.difference("Php","Python")) #{'s', 'C', 'F', 'i'}
# #对称差集 symmetric_difference 去除相同的元素剩下所有元素
# print(s.symmetric_difference("Python")) #{'C', 'y', 't', 'P', 'o', 'n', 'F', 'i', 's'}
# print(s)
# print(s <= set("FishC")) #True 检测子集
# print(s < set("FishC")) #False 检测真子集
# print(s < set("FishC.com.cn")) #True 检测真子集
# print(s > set("FishC")) #False 检测真超集
# print(s >= set("FishC")) #True 检测超集
# print(s | {1,2,3} | set("Python"))#并集 {1, 's', 2, 3, 'y', 't', 'h', 'C', 'o', 'i', 'F', 'n', 'P'}
# print(s & set("Php") & set("Python"))#交集 {'h'}
# print(s-set("Php") - set("Python"))#差集 {'F', 'C', 's', 'i'}
# print(s ^ set("Python"))#对称差集 {'y', 'C', 'i', 'P', 't', 'n', 'o', 's', 'F'}

t = frozenset("FishC") #不可变的集合
print(t) #frozenset({'C', 'F', 's', 'h', 'i'})
#仅适用于frozenset方法 会对集合数据进行改变
#update（*others）others表示支持多个参数 other仅支持一个
s = set("FishC")
print(s) #{'F', 'i', 'h', 'C', 's'}
s.update([1,1],"23")
print(s) #{'2', 1, 'F', 'i', 'h', '3', 'C', 's'}
#t.update([1,1],"23") #error
#intersection_update(*others) 交集
#difference_update(*others) 差集
#symmetric_difference_update(others) 对称差集
s.intersection_update("FishC")
print(s) #{'s', 'h', 'i', 'C', 'F'}
s.difference_update("Php","Python")
print(s) #{'s', 'i', 'C', 'F'}
s.symmetric_difference_update("Python")
print(s) #{'s', 'h', 't', 'y', 'i', 'C', 'n', 'o', 'P', 'F'}
#add(elem) 添加元素
s.add("45")
print(s)#{'C', 's', 'o', 'F', 'P', 'i', 't', 'n', 'y', '45', 'h'}
#remove(elem)静默处理 discard(elem)抛出异常 删除
#s.remove("瓦迈") #error
#s.discard("瓦迈")
#pop 随机从集合弹出一个元素
print(s.pop()) #C
print(s.pop()) #F
print(s.pop()) #s
print(s) #{'i', 'o', 'n', 't', 'P', 'h', '45', 'y'}
#clear 清空
s.clear()
print(s) #set()
#可哈希
#hash(obj) 获取一个哈希值
print(hash(1)) #1
print(hash(1.0)) #1
print(hash(1.001)) #2305843009213441
print(hash("FishC"))
#print(hash([1,2,3])) #error
#print(hash(1,2,3)) #6758511963258181749
print({"Python":520,"FishC":1314})
#print({[1,2,3]:"FishC"}) #error
print({"Python","FishC",520,1314})
x= {1,2,3}
#y = {x,4,5}#error
z = frozenset(x)
y = {z,4,5}
print(y) #{frozenset({1, 2, 3}), 4, 5}


