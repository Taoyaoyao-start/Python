# temp = input("不妨猜一下数字")
# guess = int(temp)
#
# if guess == 8:
#     print("猜对啦")
#     print("猜对也没有奖励")
# else:
#     print("猜错了")
# print("game over")
#
# x = 3
# print(x)
import random

# print('I love China.') #single quotes 单引号
# print("I love FishC.") #double quotes 双引号

#
# print("\"Life is short,let\'s learn Python.\"")#\转义字符
# print('\"Life is short,let\'s learn Python.\"')#\转义字符
#
# print("D:\\three\\two\\one\\now")
# print(r"D:\three\two\one\now")

#\放在末尾表示程序未结束
#
# print("      \n\
#          @       ")

# print('"Life is short,you need Python."') #triple quotes 三引号
#要前呼后应

#字符串的加分与乘法

# temp = input("你是谁：")
# print(temp)

# temp = input("请输入一个数字：")
# guess = int(temp)
# print(guess)

# import random
#
# counts = 3
# answer = random.randint(1,10)
# while counts > 0:
#     temp = input("不妨猜一下数字")
#     guess = int(temp)
#     if guess == answer:
#         print("猜对啦")
#         print("猜对也没有奖励")
#         break
#     else:
#         if guess < answer:
#             print("小啦")
#         else:
#             print("大啦")
#         counts = counts - 1
# print("game over")



# counts = 3
# while counts > 0:
#     print("ilovefishc.com")
#     counts = counts - 1

# import random
# random.randint(1,10)
#获取随机数种子

# x = random.getstate()
# print(x)
# random.randint(1,10)
# random.randint(1,10)
# random.randint(1,10)
# random.setstate(x)
# random.randint(1,10)
# random.randint(1,10)
# random.randint(1,10)

# print(6/2)
# print(0.1+0.2)

#decimal模块 十进制模块 精确计算浮点数
# import decimal
# a = decimal.Decimal('0.1')
# b = decimal.Decimal('0.2')
# print(a+b)
# c = decimal.Decimal('0.3')
# print(c == a + b)

#E 科学计数法
#0.00005  5e-05
#复数 1+2j
#(1+2j)  x = 1+2j  x.real(实部) x.imag(虚部)

# // 地板除 得到比目标小的最大的整数
# print(3 // 2)  1
#print(-3 // 2)  -2

# % 余数
# print(3 % 2)
# print(6 % 2)
# x == (x // y)*y + (x % y)
#divmod(a,b) 得到2个数的地板除和余数
# print(divmod(3,2))
# y = divmod(-3,2)
# print(y)

# abs(x) 绝对值
# print(abs(-520))
# print(abs(1+2j)) 返回复数的模

# print(int('520'))520
# print(int(3.14))3
# print(float('3.14'))3.14
# print(float(520))520.0
# print(float('+1E6'))1000000.0
# print(complex("1+2j")) (1+2j)

#pow 次方
# print(pow(2,3))  8
# print(pow(2,-3)) 0.125
# print(pow(2,3,5)) 2 ** 3 % 5  3

#布尔类型 bool
# print(bool(250)) True
# print(bool("假")) True
# print(bool("False")) True
# print(bool(False)) False
# print(bool(" ")) True
# print(bool(250)) True
# print(bool(0)) False
# print(bool(0.0)) False
# print(bool(0j)) False

# if 520 > 250:
#     print("大")
# else:
#     print("小")
#
# if bool(250):
#     print("True")
# else:
#     print("False")

# print(1 == True) True
# print(0 == False) True
# print(True - False) 1
# print(True + False) 1
# print(True * False) 0
# print(True / False) ERROR 布尔类型就是特殊的整数类型

#逻辑运算符
#and 左右同时为True 才为True
# print(3<4 and 4 < 5) True
# print(3 > 4 and  4 < 5) False
# print(3 < 4 and  4 > 5) False
# print(3 > 4 and  4 > 5) False
#or 左右其中一个为True 结果为TruE
# print(3<4 and 4 < 5) True
# print(3 > 4 and  4 < 5) False
# print(3 < 4 and  4 > 5) False
# print(3 > 4 and  4 > 5) False
#not 结果得到与当前bool类型相反的值
# print(not True) False
# print(not  False) True
# print(not 250) False
# print(not 0) True

# print(3 and 4) 4
# print(4 or 5) 4
# print("FishC" and "Love") Love

# or < and < not

# if 3 < 5 :
#     print("1")
#     print("2")
# print("3")

# if "小甲鱼" == "小姐姐":
#     print("1")
# else:
#     print("2")

# score = input("输入一个成绩")
# score = int(score)
# if 0<= score < 60:
#     print("D")
# elif 60 <= score < 80:
#     print("C")
# elif 80<= score <90:
#     print("B")
# elif 90 <= score < 100:
#     print("A")
# else:
#     print("S")

# age = 16
# if age < 18:
#     print("1")
# else:
#     print("2")

# print("1") if age < 18 else print("2")

# a = 3
# b = 5
# small = a if a < b else b

# score  = 66
# level = ('D' if 0 <= score < 60 else
#          'C' if 60 <= score < 80 else
#          'B' if 80 <= score <90 else
#          'A' if 90 <= score <100 else
#          print("请输入正确的数值"))

# age = 18
# isMale = True
# if age < 18:
#     print("1")
# else:
#     if isMale = True:
#         print("2")
#     else:
#         print("3")

# love = "yes"
# while love == "yes":
#     love = input("今天你还爱我吗？")

# i= 1
# sum = 0
# while i <= 100000:
#     sum += i
#     i += 1
# print(sum)

# 死循环
# while True:
#     print("没有灵魂的代码")

#break语句
# while True:
#     answer = input("可以吗")
#     if answer == "可以":
#         break

#continue语句
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i) #1 3 5 7 9

#else语句
# i = 1
# while i < 5:
#     print("循环体内，i的值是",i)
#     if i == 2:
#         break
#     i += 1
# else:
#     print("循环外，i的值是",i)

# day = 1
# while day <= 7:
#     answer = input("今天有好好学习吗？")
#     if answer != "有":
#         break
#     day += 1
# else:
#     print("非常棒，你已经坚持学习了7天")

#循环结构嵌套
#99乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
        # print(j,"*",i,"=",j * i,end = " ") #end = " "表示在输出完前面的内容之后再输出一个空格做结尾
    #     j += 1
    # print()
    # i += 1

# day = 1
# hour = 1
# while day <= 7:
#     while hour <= 8:
#         print("今天，我一定要坚持学习8个小时！")
#         hour += 1
#         if hour > 1:
#             break
#     day += 1

# for each in "FISHC":
#     print(each) #F I S H C

# for i in range(10):
#     print(i)  #0 1 2 3 4 5 6 7 8 9
#
# for i in range(11):
#     print(i) #0 1 2 3 4 5 6 7 8 9 10
#
# for i in range(5,10):
#     print(i) #5 6 7 8 9
#
# for i in range(5,10,2):
#     print(i) #5 7 9
#
# for i in range(10,5,-2):
#     print(i) #10 8 6
#
# sum = 0
# for i in range(100001):
#     sum += i
# print(sum) #5000050000

# for n in range(2,10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n,"=",x,"*",n // x)
#             break
#     else:
#         print(n,"是一个素数")

# #列表
# [1,2,3,4,5]
# rhyme = [1,2,3,4,5,"上山打老虎"]
# print(rhyme) #[1, 2, 3, 4, 5, '上山打老虎']
# #序列
# for each in rhyme:
#     print(each) #1 2 3 4 5 '上山打老虎'
# #索引
# print(rhyme[0]) #1
# print(rhyme[1]) #2
# print(rhyme[5]) #上山打老虎
#
# length = len(rhyme)
# print(rhyme[length-1]) #上山打老虎
# print(rhyme[-1]) # 上山打老虎
# print(rhyme[0:3]) #[1, 2, 3]
# print(rhyme[:3]) #[1, 2, 3]
# print(rhyme[3:]) #[4, 5, '上山打老虎']
# print(rhyme[:]) #[1, 2, 3, 4, 5, '上山打老虎']
# print(rhyme[0:6:2]) #[1, 3, 5]
# print(rhyme[::2]) #[1, 3, 5]
# print(rhyme[::-2]) #['上山打老虎', 4, 2]
# print(rhyme[::-1]) #['上山打老虎', 5, 4, 3, 2, 1]

#列表 增 删 改 查
#增 append extend
# heros = ["钢铁侠","绿巨人"]
# heros.append("黑寡妇")
# heros.extend(["鹰眼","灭霸","雷神"])
# s = [1,2,3,4,5]
# #切片
# s[len(s):] = [6]
# s[len(s):] = [7,8,9]
# #insert()
#
# s = [1,3,4,5]
# s.insert(1,2)
# s.insert(0,0)
# s.insert(len(s),6)
#
# #删 remove(指定元素) pop（下标） clear(清除)
# heros.remove("灭霸")
# print(heros) #['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '雷神']
# heros.pop(2)
# print(heros) #['钢铁侠', '绿巨人', '鹰眼', '雷神']
# heros.clear()
# print(heros) #[]

#改
# heros = ["钢铁侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
# heros[4] = "蜘蛛侠"
# print(heros) #['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '蜘蛛侠', '雷神']
# heros[3:] = ["武松","林冲","李逵"]
# print(heros) #['钢铁侠', '绿巨人', '黑寡妇', '武松', '林冲', '李逵']
#
# nums = [3,1,9,6,8,3,5,3]
# nums.sort()
# print(nums) #[1, 3, 3, 3, 5, 6, 8, 9]
# nums.reverse()
# print(nums) #[9, 8, 6, 5, 3, 3, 3, 1]
# heros.reverse()
# print(heros) #['李逵', '林冲', '武松', '黑寡妇', '绿巨人', '钢铁侠']
#
# nums = [3,1,9,6,8,3,5,3]
# #s.sort(key=None,reverse=False)
# nums.sort(reverse=True)
# print(nums) #[9, 8, 6, 5, 3, 3, 3, 1]
#
# #查 count index
# print(nums.count(3)) # 3
# print(heros.index("绿巨人")) # 4
# heros[heros.index("绿巨人")] = "神奇女侠"
# print(heros) #['李逵', '林冲', '武松', '黑寡妇', '神奇女侠', '钢铁侠']
# nums = [3,1,9,6,8,3,5,3]
# print(nums.index(3)) # 0
# #index(x,start,end)
# print(nums.index(3,1,7)) #5
# #copy(shall浅拷贝)
# nums_copy1 = nums.copy()
# print(nums_copy1) #[3, 1, 9, 6, 8, 3, 5, 3]
# nums_copy2 = nums[:]
# print(nums_copy2) #[3, 1, 9, 6, 8, 3, 5, 3]

#列表的加法
# s = [1,2,3]
# t = [4,5,6]
# print(s+t) #[1, 2, 3, 4, 5, 6]
# print(s * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# #嵌套列表
# matrix = [[1,2,3],[4,5,6],[7.8,9]]
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print(matrix) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #矩阵 matrix
#
# #访问嵌套列表
# for i in matrix:
#     for each in i:
#         print(each) #1 2 3 4 5 6 7 8 9
#
# for i in matrix:
#     for each in i:
#         print(each,end=' ')
#     print() #1 2 3    4 5 6   7 8 9
#
# print(matrix[0]) #[1, 2, 3]
# print(matrix[0][0]) #1
# print(matrix[1][1]) #5
#
# A = [0] * 3
# for i in range(3):
#     A[i] = [0] * 3
# print(A) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# B = [[0] * 3] * 3
#
# A[1][1] = 1
# print(A) #[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# B[1][1] = 1
# print(B) #[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
#
# #is 检验两个变量是否指向同一个对象的一个运算符
# x = "FishC"
# y = "FishC"
# print(x is y) #True
#
# x = [1,2,3]
# y = [1,2,3]
# print(x is y) #False
#
# print(A[0] is A[1]) #False
# print(A[1] is A[2]) #False
# print(B[0] is B[1]) #True
# print(B[1] is B[2]) #True

# x = [1,2,3]
# y = x
# print(y)

#浅拷贝
# x = [1,2,3]
# y = x.copy()
# x[1] = 1
# print(x) #[1, 1, 3]
# print(y) #[1, 2, 3]
#
# x = [[1,2,3],[4,5,6],[7,8,9]]
# y = x.copy()
# x[1][1] = 0
# print(x) #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# print(y) #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
#
# #深拷贝
# import  copy
# #浅拷贝
# x = [[1,2,3],[4,5,6],[7,8,9]]
# y = copy.copy(x)
# x[1][1] = 0
# print(x) #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# print(y) #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# #深拷贝
# x = [[1,2,3],[4,5,6],[7,8,9]]
# y = copy.deepcopy(x)
# x[1][1] = 0
# print(x) #[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# print(y) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# oho = [1,2,3,4,5]
# for i in range(len(oho)):
#     oho[i] = oho[i] * 2
# print(oho) #[2, 4, 6, 8, 10]
#
# #列表推导式[expression for target in iterable]
# oho = [1,2,3,4,5]
# oho = [i*2 for i in oho]
# print(oho) #[2, 4, 6, 8, 10]
#
# x = [i for i in range(10)]
# print(x) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# x = [i+1 for i in range(10)]
# print(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# x = []
# for i  in range(10):
#     x.append(i+1)
# print(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# y = [c*2 for c in "FishC"]
# print(y) #['FF', 'ii', 'ss', 'hh', 'CC']
#
# code = [ord(c) for c in "FishC"]
# print(code) #[70, 105, 115, 104, 67]
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# col2 = [row[1] for row in matrix]
# print(col2) #[2, 5, 8]
#
# diag = [matrix[i][i] for i in range(len(matrix))]
# print(diag)
#
# diag2 = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
# print(diag2)

# s = [[0]*3 for i in range(3)]
# print(s) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# s[1][1] = 1
# print(s) #[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
#
# even = [i for i in range(10) if i%2 == 0]
# print(even) #[0, 2, 4, 6, 8]
#
# even = [i+1 for i in range(10) if i%2 == 0]
# print(even) #[1, 3, 5, 7, 9]
#
# words = ["Great","FishC","Brilliant","Excellent","Fantistic"]
# fwords = [w for w in words if w[0] == 'F']
# print(fwords) #['FishC', 'Fantistic']
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# flatten = [col for row in matrix for col in row]
# print(flatten) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# flatten = []
# for row in matrix:
#     for col in row:
#         flatten.append(col)
# print(flatten) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# fla = [x+y for x in "fishc" for y in "FISHC"]
# print(fla) #['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI',.....
#
# fla2 = []
# for x in "fishc":
#     for y in "FISHC":
#         fla2.append(x+y)
# print(fla2) #['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI',.....
#
# even2 = [[x,y] for x in range(10) if x% 2 == 0 for y in range(10) if y % 3 == 0]
# print(even2) #[[0, 0], [0, 3], [0, 6], [0, 9], [2, 0],.....
#
# _ = []
# for x in range(10):
#     if x % 2==0:
#         for y in range(10):
#             if y % 3 == 0:
#                 _.append([x,y])
# print(_) #[[0, 0], [0, 3], [0, 6], [0, 9], [2, 0],.....

#KIS   Keep It Simple $ Stupid

#元组 用的是（） 列表用[]
# rhyme = (1,2,3,4,5,"上山打老虎")
# print(rhyme) #(1, 2, 3, 4, 5, '上山打老虎')
# rhyme = 1,2,3,4,5,"上山打老虎"
# print(rhyme) #(1, 2, 3, 4, 5, '上山打老虎')
# print(rhyme[0]) #1
# print(rhyme[-1]) #上山打老虎
# #元组不可变 修改元组的行为不可去
# #rhyme[1] = 10 #error
# #支持切片
# print(rhyme[:]) #(1, 2, 3, 4, 5, '上山打老虎')
# print(rhyme[::-1]) #('上山打老虎', 5, 4, 3, 2, 1)
#
# #元组只支持查 count index
# nums = (3,1,9,6,8,3,5,3)
# print(nums.count(3)) #3
#
# heros = ("zzx","ljr","hgf")
# print(heros.index("hgf")) #2
#
# s = (1,2,3)
# t = (4,5,6)
# print(s+t) #(1, 2, 3, 4, 5, 6)
# print(s*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)
# w = s,t
# print(w) #((1, 2, 3), (4, 5, 6))
# for each in s:
#     print(each) #1 2 3
# for i in w:
#     for each in i:
#         print(each) #1 2 3 4 5 6
#
# s = (1,2,3,4,5)
# print([each*2 for  each in s]) #[2, 4, 6, 8, 10]
# print((each*2 for each in s)) #<generator object <genexpr> at 0x000001BBA83436B0>
#
# x = (520)
# print(type(x)) #<class 'int'>
# x = (520,)
# print(type(x)) #<class 'tuple'>
#
# #打包和解包
# t = (123,"FishC",3.14) #建立一个元组就是打包行为
# #将他们一次性赋值给三个变量名的行为就是解包
# x,y,z = t
# print(x) #123
# print(y) #FishC
# print(z) #3.14
# #同样适用于任何的序列类型
# t = [123,"FishC",3.14]
# x,y,z = t
# print(x) #123
# print(y) #FishC
# print(z) #3.14
#
# a,b,c,d,e = "FishC"
# print(a) #F
# print(b) #i
# print(c) #s
# print(d) #h
# print(e) #C
# a,b,*c = "FishC"
# print(a) #F
# print(b) #i
# print(c) #['s', 'h', 'C']
#
# s = [1,2,3]
# t = [4,5,6]
# w = (s,t)
# print(w) #([1, 2, 3], [4, 5, 6])
# w[0][0] = 0
# print(w) #([0, 2, 3], [4, 5, 6])

#字符串
# x = "12321"
# print("yes" if x == x[::-1] else "no") #yes
# #46个方法
#大小写字母换来换去
# capitalize() casefold() title()
#swapcase() upper() lower()
# x = "I love FishC"
# print(x.capitalize()) #I love fishc 首字母大写
# print(x.casefold()) #i love fishc 所有字母小写
# print(x.title()) #I Love Fishc 每个字母首字母大写 其余小写
# print(x.swapcase()) #i LOVE fISHc 大小写翻转
# print(x.upper()) #I LOVE FISHC 所有字母大写
# print(x.lower()) #i love fishc 所有字母小写（只能处理字母）

#左中右对齐 center(width,fillchar='') ljust(width,fillchar='')
#rjust(width,fillchar='') zfill(width)
# x = "有内鬼，停止交易！"
# print(x.center(5)) #有内鬼，停止交易！
# print(x.center(15)) #   有内鬼，停止交易！
# print(x.ljust(15)) #有内鬼，停止交易！
# print(x.rjust(15)) #      有内鬼，停止交易！
# print(x.zfill(15)) #000000有内鬼，停止交易！
# print("520".zfill(5)) #00520
# print(x.center(15,"淦")) #淦淦淦有内鬼，停止交易！淦淦淦
# print(x.ljust(15,"淦")) #有内鬼，停止交易！淦淦淦淦淦淦
#
#查找 count(sub[,start[,end]]) find(sub[,start[,end]]) rfind(sub[,start[,end]])
#index(sub[,start[,end]]) rindex(sub[,start[,end]])
# x = "上海自来水来自海上"
# print(x.count("海"))# 2  #出现的次数
# print(x.count("海",0,5)) #1
# #find(从左往右) rfind（从右往左） 子字符串在字符串中的索引下标值
# print(x.find("海")) #1
# print(x.rfind("海")) #7
# #index rindex 区别：如果定位不到子字符串处理方式不同
# print(x.find("鬼")) #-1
# print(x.index("鬼")) #error

#替换 expandtabs([tabsize=8]) replace(old,new,count=-1)
#translate(table)
# code = """
#     print("I love FishC)
#     print("I love my wife)"""
# new_code = code.expandtabs(4)
# print(new_code)#使用空格替换制表符(tab)
# print("在吗!我在你家楼下!!".replace("在吗","想你")) #想你!我在你家楼下!!
# table = str.maketrans("ABCDEFG","1234567")
# print("I love FishC".translate(table)) #I love 6ish3
# print("I love FishC".translate(str.maketrans("ABCDEFG","1234567"))) #I love 6ish3
# print("I love FishC".translate(str.maketrans("ABCDEFG","1234567","love"))) #I  6ish3 多一个参数指将指定字符串忽视

#判断 startswith(prefix[,start[,end]]) endswith(suffix[.start[,end]])
#isupper() islower()
#istitle() isalpha() isascii() isspace() isprintable()
#isdecimal() isdigit() isnumeric() islnum() isidentifier(）
#判断指定字符串是否在字符串的起始位置 startswith(prefix[,start[,end]])
# x = "我爱Python"
# print(x.startswith("我")) #True
# print(x.startswith("小甲鱼")) #False
# print(x.endswith("Python"))#True
# print(x.endswith("Py")) #False
# print(x.startswith("我",1)) #False 表示从索引值1开始配对
# print(x.startswith("爱",1)) #True
# print(x.endswith("Py",0,4)) #True
#
# x = "她爱Python"
# if x.startswith(("你","我","她")):
#     print("总有人喜欢Python") #总有人喜欢Python
#
#判断所有单词是否都是以大写字母开头其余字母为小写 istitle()
# x = "I love Python"
# print(x.istitle()) #False
# #判断所有字母是大写 isupper()
# print(x.isupper()) #False
# print(x.upper().isupper()) #True
# #判断字符串是否都是有字母构成 isalpha()
# print(x.isalpha()) #False
# print("IlovePythoin".isalpha()) #True
# #判断是否为空白字符串 isspace()
# print("   \n".isspace()) #True
# #是否所有字符可打印 isprintable()
# print(x.isprintable()) #True
# print("I love FishC\n".isprintable()) #False
# #判断数字 isdecimal() isdigit() isnumeric()
# x = "12345"
# print(x.isdecimal()) #True
# print(x.isdigit()) #True
# print(x.isnumeric()) #True
# x = "2²"
# print(x.isdecimal()) #False
# print(x.isdigit()) #True
# print(x.isnumeric()) #True
# x = "ⅠⅡⅢ"
# print(x.isdecimal()) #False
# print(x.isdigit()) #False
# print(x.isnumeric()) #True
# x = "一二三"
# print(x.isdecimal()) #False
# print(x.isdigit()) #False
# print(x.isnumeric()) #True
# #集大成者 isalnum() = isalpha() isdecimal() isdigit() isnumeric()
# #判断一个字符串是否为合法的Python标识符isidentifier(）
# print("I am a good gay".isidentifier()) #False
# print("I_am_a_good_gay".isidentifier()) #True
# print("520Fishc".isidentifier()) #False
# #判断是否为保留标识符：if while else。。。
# import keyword
# print(keyword.iskeyword("if")) #True
# print(keyword.iskeyword("Py")) #False

#截取 strip(chars=None) lstrip(chars=None) rstrip(chars=None)
#removeprefix(prefix) removesuffix(suffix)
# print("    左侧不要留白".lstrip()) #左侧不要留白
# print("右侧不要留白    ".rstrip()) #右侧不要留白
# print("  左右不要留白    ".strip()) #左右不要留白
# #无论从左还是从右开始，只要碰到不是wcom.这五个字符就停止截取
# print("www.ilovefishc.com".lstrip("wcom.")) #ilovefishc.com
# print("www.ilovefishc.com".rstrip("wcom.")) #www.ilovefish
# print("www.ilovefishc.com".strip("wcom.")) #ilovefish
# #removeprefix(prefix) removesuffix(suffix)
# #允许指定将要删除的前缀后缀
# print("www.ilovefishc.com".removeprefix("www.")) #ilovefishc.com
# print("www.ilovefishc.com".removesuffix(".com")) #www.ilovefishc
#
# #拆分&拼接 partition(sep) rpartition(sep)
# #将字符串以参数指定的分隔符为依据进行切割 将切割后的结果返回一个三元组
# print("www.ilovefishc.com".partition(".")) #('www', '.', 'ilovefishc.com')
# print("www.ilovefishc.com".rpartition(".")) #('www.ilovefishc', '.', 'com')
# #split(sep=None,maxsplit=-1) 次数
# print("苟日新，日日新，又日新".split()) #['苟日新，日日新，又日新']
# print("苟日新，日日新，又日新".split('，')) #['苟日新', '日日新', '又日新']
# print("苟日新，日日新，又日新".rsplit('，')) #['苟日新', '日日新', '又日新']
# print("苟日新，日日新，又日新".split('，',1)) #['苟日新', '日日新，又日新']
# print("苟日新，日日新，又日新".rsplit('，',1)) #['苟日新，日日新', '又日新']
# print("苟日新\n日日新\n又日新".split('\n')) #['苟日新', '日日新', '又日新']
# print("苟日新\r日日新\r又日新".split('\r')) #['苟日新', '日日新', '又日新']
# #splitlines(keepends=False) 将字符串按行进行分割将结果以列表返回
# print("苟日新\n日日新\n又日新".splitlines()) #['苟日新', '日日新', '又日新']
# print("苟日新\r日日新\r又日新".splitlines()) #['苟日新', '日日新', '又日新']
# print("苟日新\r日日新\n又日新".splitlines()) #['苟日新', '日日新', '又日新']
# #参数指定是否包含换行符 如果是True就包含换行符 默认False不包含
# #join(iterable)
# print(".".join(["www","ilovefishC","com"])) #www.ilovefishC.com
# print("^".join(("F","ish","C"))) #F^ish^C
# print("".join(("FishC","FishC"))) #FishCFishC

#格式化字符串 format
# year = 2010
# print("鱼C工作室成立于{}年".format(year)) #鱼C工作室成立于2010年
# print("1+2={},2的平方是{},3的立方是{}".format(1+2,2*2,3*3*3)) #1+2=3,2的平方是4,3的立方是27
# print("{}看到{}就很激动".format("小甲鱼","漂亮的小姐姐")) #小甲鱼看到漂亮的小姐姐就很激动
# print("{1}看到{0}就很激动".format("小甲鱼","漂亮的小姐姐")) #漂亮的小姐姐看到小甲鱼就很激动
# print("{0}{0}{1}{1}".format("是","非")) #是是非非
# print("我叫{name},我爱{fav}".format(name="小甲鱼",fav="Python")) #我叫小甲鱼,我爱Python
# print("{},{},{}".format(1,"{}",2)) #1,{},2
# print("{},{{}},{}".format(1,2)) #1,{},2
#[[fill]align][sign][#][0][width][grouping_option][.precision][type]
#[align] 对齐的方式 '<' 左对齐 '>' 右对齐 '=' 强制将填充放置在符号之后但在数字之前 '^' 居中
# print("{:^}".format(250)) #250
#[width] 指定宽度
# print("{:^10}".format(250)) #   250
# print("{1:>10}{0:<10}".format(520,250)) #       250520
# print("{left:>10}{right:<10}".format(right=520,left=250)) #       250520
#[0] 数字类型启用感知正负号的0填充效果 只对数字有效
# print("{:010}".format(520)) #0000000520
# print("{:010}".format(-520)) #-000000520
# print("{1:%>10}{0:%<10}".format(520,250)) #%%%%%%%250520%%%%%%%
# print("{:0=10}".format(520)) #0000000520
# print("{:0=10}".format(-520)) #-000000520
#[sign] '+'正数在前面添加正号，负数在前面添加负号 ’-‘只有负数在前面添加符号 ’空格’正数在前面添加一个空格，复数在前面添加负号
print("{:+}{:-}".format(520,-250)) #+520-250
print("{:,}".format(1234)) #1,234
print("{:_}".format(1234)) #1_234
print("{:,}".format(123)) #123
print("{:,}".format(123456789)) #123,456,789
#[type] 精度 设置为‘f’或'F'的浮点数来说，是限定小数点后显示多少个数位
#设置位‘g’或'G'的浮点数来说，是限定小数点前后一共显示多少个数位
#对于非数字类型来说，限定的是最大字段的大小
#对于整数类型来说，则不允许使用[.precision]选项
print("{:.2f}".format(3.1415)) #3.14
print("{:.2g}".format(3.1415))  #3.1
print("{:.6}".format("I love FishC")) #I love
#print("{:.2}".format(520)) error
# 'b' 二进制 'c'Unicode字符的形式输出 'd'十进制 'o'八进制输出
# ‘x’十六进制 'n'与‘d’类似，不同在于会使用当前语言环境设置的分隔符插入到恰当位置
# None 与‘d’一样
print("{:b}".format(80)) #1010000
print("{:c}".format(80)) #P
print("{:d}".format(80)) #80
print("{:o}".format(80)) #120
print("{:x}".format(80)) #50
#[#]自动追加前缀
print("{:#b}".format(80)) #0b1010000
print("{:#o}".format(80)) #0o120
print("{:#x}".format(80)) #0x50
#'e'科学计数法输出 'E'科学计数法输出 'f'定点表示法输出 'F'定点表示法输出
# 'g'小数以f输出 大数以e输出 'G'小数以F输出 大数以G输出
# 'n'与g类似，不同在于使用当前语言环境设置的分隔符插入到恰当位置
# '%'百分比形式输出 None与g类似不同在于使用定点表示法输出，小数点后将至少显示一位
print("{:e}".format(3.1415)) #3.141500e+00
print("{:E}".format(3.1415)) #3.141500E+00
print("{:f}".format(3.1415)) #3.141500
print("{:g}".format(123456789)) #1.23457e+08
print("{:g}".format(1234.56789)) #1234.57
print("{:%}".format(0.98)) #98.000000%
print("{:.2%}".format(0.98)) #98.00%
print("{:.{prec}f}".format(3.1415,prec=2)) #3.14
print("{:{fill}{align}{width}.{prec}{ty}}".format(3.1415,fill='+',align='^',width=10,prec=3,ty='g'))
#+++3.14+++
#f-字符串
year = 2010
print("鱼C工作室成立与{}年".format(year)) #鱼C工作室成立与2010年
print(F"鱼C工作室成立与{year}年") #鱼C工作室成立与2010年
print(F"1+2={1+2},2的平方是{2*2},3的立方是{3*3*3}") #1+2=3,2的平方是4,3的立方是27
print("{:010}".format(-520))
print(F"{-520:010}") #-000000520
print("{:,}".format(123456789))#123,456,789
print(F"{123456789:,}")
print("{:.2f}".format(3.1415)) #3.14
print(F"{3.1415:.2f}")
print("{:{fill}{align}{width}.{prec}{ty}}".format(3.1415,fill='+',align='^',width=10,prec=3,ty='g'))
fill='+'
align='^'
width=10
prec=3
ty='g'
print(F"{3.1415:{fill}{align}{width}.{prec}{ty}}") #+++3.14+++




