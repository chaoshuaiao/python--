import numpy as np
import pandas as pd 

pd.set_option('display.unicode.east_asian_width', True)
# a = np.array([[1,2,3],[4,5,6],[7,8,9.0]])
# b = np.arange(3,dtype=int).reshape(1,3)
# # print(np.append(a,b))
# print(np.concatenate((a,b),axis=0))
# print(a.shape)
# # print(np.argwhere(a==2))
# b = a[1:3,1:3]
# b[0,0] = 100
# c = np.append(a,b,axis=0)
# data = pd.DataFrame(c,index=["a","b","c","d"],columns=["g","e","f"])
# print(data)
# print(data.loc[:,'g'])
# data2 = data.iloc[0,1] 
# print(data)
'''
# print(1)'''
# print(int("102",16))
# print(oct(int("257",8)))   
# a = str("1020")
# print(a[::-1])
# sdfsdf = "1234567890"
# sdfsf   = sdfsdf[::-1]
# a = 5
# b = 3
# print(eval(a+b))
# print(eval("0*12"))
# print('abc 3 4 5'.split()[2])
# print('hello'[-2]+'world'[1])
# b = 5
# a = str(b+9)
# print(eval('a[1]'))  
# st = input()
# for i in range(1,6,2):
#     print(" "*int((10-i)/2)+st*i+" "*int((10-i)/2))

# print("ok"==True)
# print(3<5>2)
# lst =("a","b","c","d","d")
# lst = pd.Series(lst)
# print(len(lst.value_counts()))
# print(lst.value_counts().count)
# a = 40000
# print(int(str(a)[::-1]))
# for i in range(7):
#     for j in range(7):
#         for k in range(7):
#             if int(str(i*100+j*10+k),7)== int(str(k*100+j*10+i),9):
#                 print(int(str(i*100+j*10+k),7))
# print('ok')
# x,y = 20,30
# def dkk(x):
#     # global y
#     y = x +2
#     return y
# print(dkk(8))
# print(y)

# 参数传递，位置优先？        
# def sk(n,m):
#     if n == 0:
#         return m
#     elif m == 0:
#         return n
#     else:
#         if n >= m:
#             print('n>m',n,m)
#             return sk(m,n-m)+1
            
#         else:
#             print('m>n',n,m)
#             return sk(n,m-n)+2
            
# print(sk(3,4))

#*args参数为元组，可以接收任意多个参数，但必须放在最后
# def f(x,y,*args):
#     return x+y+sum(args)
# print(f(1,2,3,4,5))

#**kwargs参数为字典，可以接收任意多个键值对参数，但必须放在最后
# def f(x,y,**kwargs):
#     return x+y+sum(kwargs.values())
# print(f(1,2,a=3,b=4,c=5))

#未解决
# def kjk(f,g):
#     return f(g(x))
# def ddd(x):
#     return x+1
# def sss(x):
#     return x*2
# x = int(input())
# f = kjk(sss,ddd)
# print(f(x))

#从右向左查找第几位
# print('sjdklffkjlk'.rfind('ff'))


# print(f"lambda x: s= str(x);l=len(str(x));for i in range(l): en = "".join(s[-1-i] return en")
# s = str(a)
# l = len(s)
# for i in range(l):
#     en = "".join(s[-1-i])
#     print(en,end="")

# a = list(list(range(10)))
# b = tuple(a)
# print(a,a[1:5])
# print(b,b[1:5])
# tup2 = (1,2,3,4,5,6,7)
# print(tup2[1:5])

#函数中的x，y为引用传递，修改后会影响到外部变量的值，data为值传递，修改后不会影响到外部变量的值
# def fun(x,y):
#     x = x+2
#     y.append(2)
#     print(x,y)
# x= 0
# y=[0]
# fun(x,y)
# print(x,y)    

# a = [1,2,3,4,5]
# a.append(20)
# print(a)

#map函数，将后面的字符串按顺序映射到前面的函数上，返回一个迭代器
# a = map(lambda x: int(x[-1]),input().split())
# for e in a:
#     print(e,end=" ")


#a.copy()是浅拷贝，copy.deepcopy()是深拷贝、
# import copy
# def fun():
#     a = []
#     for i in range(3):
#         a.append([0]*3)
#     print(a)
#     b=copy.deepcopy(a)
#     print(b)
#     b[1][1] = 100
#     print(a)
#     print(b)
#     a[1][1] = 200
#     print(a)
#     print(b)
# fun()

#内循环为行，外循环为列，内循环内设置元素
# a = [[x for i in range(1,4)] for x in range(1,5)]
# print(a)
# # for i in a:
# #     for j in i:
# #         print(j,end=" ")
# #     print()

#filter函数，过滤掉不符合条件的元素，返回一个迭代器
# s = filter(lambda x :x%2!=0,map(lambda x:x%10,[45,65,44,88]))
# print(list(s))


# f = open(r"D:\桌面\ads.txt",'r')
# write = f.readlines()
# f.close()
# s = ""
# for i in write:
#     index = i.index("entry: ")
#     s += i[index+7:]
# print(s)


# with open(r"D:\桌面\新建文本文档.txt",'r') as f:
#     a = f.read().split()
#     set_a = set(a)
# with open(r"D:\桌面\常用文件\ads.txt\vungle.txt",'r') as f:
#     b = f.read().split()
#     set_b = set(b)
# if len(a)!= len(b):
#     print("文件长度不一致")
#     if len(set_a) > len(set_b):
#         print("set_a > set_b")
#         for i in set_a:
#             if i not in set_b:
#                 print(i)          
#     else:
#         print("set_b > set_a")
#         for i in set_b:
#             if i not in set_a:
#                 print(i)    
# else:
    # print("文件内容一致")








