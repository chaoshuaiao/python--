import shutil
import os
#!/usr/bin/python3
import re
 
line = re.match("(\w+) (\w+)(.)", "hello world!ss")
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
print(line.group(1))
print(line.group(2))
print(line.group(3))
print(line.groups())
print(line.string)   


# print(type(matchObj))
# if matchObj:
#    print ("matchObj.group() : ", matchObj.groups())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2)) 
# else:
#    print ("No match!!")


# print("hello wor\nld2")

# shutil.copyfile("hello2.py","f:\python文件\pandas\正则表达式.py")#复制文件到指定文件夹