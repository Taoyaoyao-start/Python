#字典是Python中唯一实现映射关系的内置类型
c_table = [".-"]
d_table = ["A"]
code = input("请输入摩斯密码:")
split_code = code.split(" ")

result = [d_table[c_table.index(each)]for each in split_code]
result = []
# for each in split_code:
#     _ = c_table.index(each)
#     result.append(d_table[_])
print(result)
#方法2
c_table=[".-","A"]
code = input("请输入摩斯密码:")
split_code = code.split(" ")

result = [c_table[c_table.index(each)+1] for each in split_code]
print(result)
#方法3  字典方式
c_table = {".-":"A"}
code = input("请输入摩斯密码:")
split_code = code.split(" ")

result = [c_table[each] for each in split_code]
print(result)
x = {"吕布","关羽"}
print(type(x)) #<class 'set'>
y = {"吕布":"奉先","关羽":"云长"}
print(type(y)) #<class 'dict'>
print(y["吕布"]) #奉先
y["刘备"] = "玄德"
print(y) #{'吕布': '奉先', '关羽': '云长', '刘备': '玄德'}
#dict函数 用来建立字典的
a = {"吕布":"奉先","关羽":"云长","刘备": "玄德"}
b = dict(吕布="奉先",关羽="云长",刘备="玄德")
c = dict([("吕布","奉先"),("关羽","云长"),("刘备","玄德")])
d = dict({"吕布":"奉先","关羽":"云长","刘备": "玄德"})
e = dict({"吕布":"奉先","关羽":"云长"},刘备="玄德")
f = dict(zip(["吕布","关羽","刘备"],["奉先","云长","玄德"]))
print(a == b == c == d == e == f) #True
#增 fromkeys(iterable[,values])
d = dict.fromkeys("Fish",250)
print(d) #{'F': 250, 'i': 250, 's': 250, 'h': 250}
d['F'] = 70
print(d) #{'F': 70, 'i': 250, 's': 250, 'h': 250}
d['C'] = 67
print(d) #{'F': 70, 'i': 250, 's': 250, 'h': 250, 'C': 67}
#删 pop（key[,default]）
print(d.pop('s')) #250
print(d) #{'F': 70, 'i': 250, 'h': 250, 'C': 67}
# print(d.pop("狗")) error
print(d.pop("狗","没有")) #没有
#popitem() 删除最后一个加入的键值对
print(d.popitem()) #('C', 67)
del d['i']
print(d) #{'F': 70, 'h': 250}
del d
#print(d) #error
d = dict.fromkeys("FishC",250)
print(d) #{'F': 250, 'i': 250, 's': 250, 'h': 250, 'C': 250}
d.clear()
print(d) #{}
#改 update([other])
d = dict.fromkeys("FishC")
d['s'] = 115
print(d) #{'F': None, 'i': None, 's': 115, 'h': None, 'C': None}
d.update({'i':105,'h':104})
print(d) #{'F': None, 'i': 105, 's': 115, 'h': 104, 'C': None}
d.update(F='70',C='67')
print(d) #{'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}
#查  get(key[,default]) setdefault(key[,default])
print(d['C']) #67
#print(d['c']) #error
print(d.get('c',"这里没有c")) #这里没有c
print(d.setdefault('C',"code")) #67
print(d.setdefault('c',"code")) #code
#items() keys() values() 分别用于获取字典的键值对，键和值三者的视图对象
keys = d.keys()
values = d.values()
items = d.items()
print(items) #dict_items([('F', '70'), ('i', 105), ('s', 115), ('h', 104), ('C', '67'), ('c', 'code')])
print(values) #dict_values(['70', 105, 115, 104, '67', 'code'])
print(keys) #dict_keys(['F', 'i', 's', 'h', 'C', 'c'])
d.pop('c')
print(d) #{'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}
print(items) #dict_items([('F', '70'), ('i', 105), ('s', 115), ('h', 104), ('C', '67')])
print(values) #dict_values(['70', 105, 115, 104, '67'])
print(keys) #dict_keys(['F', 'i', 's', 'h', 'C'])
#浅拷贝 copy
e = d.copy()
print(e) #{'F': '70', 'i': 105, 's': 115, 'h': 104, 'C': '67'}
print(len(d)) #5
print('C' in d) #True
print('c' not in d) #True
print(list(d)) #['F', 'i', 's', 'h', 'C']
print(list(d.values())) #['70', 105, 115, 104, '67']
#iter（）
e = iter(d)
print(next(e)) #F
print(next(e)) #i
print(next(e)) #s
print(next(e)) #h
print(next(e)) #C
#print(next(e))
# print(next(e)) #error
#reversed()
print(list(reversed(d.values()))) #['67', 104, 115, 105, '70']
#嵌套
d = {"吕布":{"语文":60,"数学":70,"英语":80},"关羽":{"语文":80,"数学":90,"英语":70}}
print(d["吕布"]["数学"]) #70
d = {"吕布":[60,70,80],"关羽":[80,90,70]}
print(d["吕布"][1]) #70
#字典推导式
d = {'F':70,'i':105,'s':115,'h':104,'C':67}
b = {v:k for k,v in d.items()}
print(b) #{70: 'F', 105: 'i', 115: 's', 104: 'h', 67: 'C'}
c = {v:k for k,v in d.items() if v>100}
print(c) #{105: 'i', 115: 's', 104: 'h'}
d = {x:ord(x) for x in "FishC"}
print(d)  #{'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}
d = {x:y for x in [1,3,5] for y in [2,4,6]}
print(d) #{1: 6, 3: 6, 5: 6}






