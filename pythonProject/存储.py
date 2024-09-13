#open 操作文件
# f = open("FishC.text","w")
# print(f.write("I love Python."))
# print(f.writelines(["I love FishC.\n","i love my wife."]))
# f.close()
# f = open("FishC.text","r+")
# print(f.readable()) #True 测试是否可以读
# print(f.writable()) #True 测试是否可以写
# for each in f:
#     print(each)
# print(f.read())
# print(f.tell()) #返回文件指针在文件对象中的位置
# print(f.seek(0))
# print(f.readline()) #I love Python.I love FishC.
# print(f.read()) #i love my wife.
# print(f.write("I love my WIFI"))
# print(f.flush())
# print(f.truncate(29)) #截取 截断
# print(f.close())
# f = open("FishC.text","w")
# f.close()
#处理路径 pathlib
# from pathlib import Path
# print(Path.cwd())
# p = Path('D:\JavaProject\pythonProject')
# print(p)
# q = p / "FishC.text"
# print(q)
# print(p.is_dir()) #True 判断是否为文件夹
# print(q.is_dir()) #False
# print(p.is_file()) #False 判断是否为文件
# print(q.is_file()) #TRUE
# print(p.exists()) #True 判断路径是否存在
# print(q.exists())
# print(Path("C:/404").exists()) #False
# print(p.name) #pythonProject 获取路径最后一个部分
# print(q.stem) #FishC 获取文件名
# print(q.suffix)  #.text 获取后缀
# print(p.parent)#D:\JavaProject 获取父级目录
# print(p.parents) #<WindowsPath.parents> 获取祖级
# ps = p.parents
# for each in ps:
#     print(each)
# print(p.parts)#('D:\\', 'JavaProject', 'pythonProject') 将路径各个组件拆分成元组
# print(p.stat())#查询文件或文件夹的信息
# print(q.stat().st_size)
# print(Path("./doc"))
# print(Path("../FishC"))
# print(Path("./doc").resolve())#将相对路径转化为绝对路径
# #获取当前路径下所有子文件和子文件夹
# print(p.iterdir())
# for each in p.iterdir():
#     print(each)
# print([x for x in p.iterdir() if x.is_file()])
# n = p / "FishC"#创建文件夹 mkdir
# #print(n.mkdir())
# #print(n.mkdir(exist_ok=True))
# #n = p / "FishC/A/B/C" error
# #print(n.mkdir(parents=True,exist_ok=True))
# n = n / "FishC.txt"
# print(n)
# f = n.open("w")
# f.write("I love FishC..")
# f.close()
# n.rename("NewFishC.txt")#重命名
# #m = Path("NewFishC.txt")#替换 replace
# #print(m)
# #rmdir() unlink() 删除
# n.unlink()
# n.parent.rmdir()
#with语句和上下文管理器
f = open("FishC.text","w")
f.write("I love FishC.")
f.close()
with open("FishC.text","w") as f:
    f.write("I love FishC.")
#pickle dump load
import pickle
x,y,z = 1,2,3
s = "FishC"
l = ["小甲鱼",520,3.14]
d = {"one":1,"two":2}

with open("data.pk1","wb") as f:
    pickle.dump(x,f)
    pickle.dump(y, f)
    pickle.dump(z, f)
    pickle.dump(s, f)
    pickle.dump(l, f)
    pickle.dump(d, f)
with (open("data.pk1","rb") as f):
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)
    s = pickle.load(f)
    l = pickle.load(f)
    d = pickle.load(f)
print(x,y,z,s,l,d,sep="\n")

