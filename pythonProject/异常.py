# try:
#     1/0
# except:
#     print("出错啦")
# try:
#     1/1
# except:
#     print("出错啦")
# try:
#     1/0
# except ZeroDivisionError:
#     print("出错啦")
# # try:
# #     520 + "FishC"
# # except ZeroDivisionError:
# #     print("出错啦")
# try:
#     1 /0
# except ZeroDivisionError as e:
#     print(e)
# try:
#     1/0
#     520 + "FishC"
# except(ZeroDivisionError,ValueError,TypeError):
#     pass
# try:
#     1 / 0
#     520 + "FishC"
# except ZeroDivisionError:
#     print("除数不能为0")
# except ValueError:
#     print("值不正确")
# except TypeError:
#     print("类型不正确")
try:
    1 / 0
except:
    print("逮到了")
else:
    print("没带到")
try:
    1 / 1
except:
    print("逮到了")
else:
    print("没带到")
try:
    1 / 0
except:
    print("逮到了")
else:
    print("没带到")
finally:#无论如何都会执行
    print("带没带到都会吱一声")
try:
    f = open("FishC.text","w")
    f.write("I love FishC.")
except:
    print("出错啦")
finally:
    f.close()
# try:
#     while True:
#         pass
# finally:
#     print("晚安-")
# #异常的嵌套
try:
    try:
        520 + "FishC"
    except:
        print("内部异常")
    1 / 0
except:
    print("外部异常")
finally:
    print("收尾异常")
try:
    1 / 0
    try:
        520 + "FishC"
    except:
        print("内部异常")

except:
    print("外部异常")
finally:
    print("收尾异常")
#raise语句
# raise ValueError("值不值确")
# raise FishCError("不行")
# try:
#     1 / 0
# except:
#     raise ValueError("这样可不行")
# raise ValueError("这样可不行") from ZeroDivisionError
#assert
s = "FishC"
assert s == "FishC"
# assert s != "FishC"
#利用异常来实现goto
# try:
#     while True:
#         while True:
#             for i in range(10):
#                 if i > 3:
#                     raise
#                 print(i)
#             print("被跳过")
#         print("被跳过")
#     print("被跳过")
# except:
#     print("到这来了")



