import os
import shutil
import sys



print(sys.argv[0])

#注意：路径前面加r，表示字符串为raw string，防止转义
# os.rename("hello.py","hello2.py")
# print(os.listdir("../基础学习"))
# os.mkdir(r"D:\桌面\老项目\GTA\test")从电脑复制的路径需要加r




# print(sys.argv)#输出命令行参数列表，第一个列表元素为文件名
# shutil.copyfile("hello2.py","f:\python文件\pandas/hello2.py")#复制文件到指定文件夹
#输出当前文件夹os.getcwd()
#输出当前文件夹文件以及子文件夹os.listdir（）
#判断是否是文件夹os.path.isfile()
#获取文件的大小os.path.getsize()
#添加文件夹os.mkdir（）
#删除文件夹os.rmdir（）
#删除文件os.remove（）
#文件改名以及移动os.rename(x,y)
#文件复制到指定文件夹shutil.copyfile(x,y)
#
# class dog(object):
#     def __init__(self,name):
#         self.name = name
#     def bark(self):
#         print(self.name)

# class cat(dog):
#     def __init__(self,name,big):
#         super().__init__(name)
#         self.big = big
#     def bark(self):
#         self.name = self.name + self.big
#         super().bark()

# mycat = cat(name = "Tom", big = " is big")
# mycat.bark()###继承初始化父类，并重写父类方法

# class A:
#     def __init__(self):
#         pass

# a,b = A(),A()

# dit = dict({a:1,b:2,A():3})

# print(len(dit)) 

# 输入年月日，输出星期几
# i = input().split()
# years,months,days = int(i[0]),int(i[1]),int(i[2])  
# day = 0
# monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
# for i in range(2012,years):
#     if i%4 == 0 and i % 100 !=0 or i % 400 ==0:
#         day += 366
#     else:
#         day += 365
# if years%4 == 0 and years % 100 !=0 or years % 400 ==0:
#     monthdays[1] = 29
# for i in range(months-1):
#     day += monthdays[i]
# day += days
# day -= 22
# print(day%7)

#输入字符串，将字符串大小写互换
# s = input()
# s_ = ""
# for i in s:
#     if ord(i) >= ord('a') and ord(i) <= ord('z'):
#         s_ += chr(ord(i)-32)
#     elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
#         s_ += chr(ord(i)+32)
#     else:
#         print("输入字符串有非法字符")   # "输入字符串有非法字符"
# print(s_)
# s = input()
# s_ = ""
# for i in s:
#     if i >= 'a' and i <= 'z': 
#         s_ += chr(ord(i)-32)
#     elif i >= 'A' and i <= 'Z':
#         s_ += chr(ord(i)+32)
#     else:
#         print("输入字符串有非法字符")   # "输入字符串有非法字符"
# print(s_)
# lambda x: x+1
# print(7%2)


#输入n个数组，对ng个元素进行排序，输出排序后的数组
# i = int(input())
# a = []
# for item in range(i):
#     b = input().split() 
#     a.append((b[0],int(b[1])))
# a.sort(key = lambda x:(-x[-1],x[0]))#sort方法进行排序，-x[-1]表示降序排序，x[0]表示升序排序
# for item in a:
#     print(item[0],item[1])


#try 和 except 语句
# try :
# except WXception as e:
    #     print(e)
