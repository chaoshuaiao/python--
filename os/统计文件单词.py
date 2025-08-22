
from multiprocessing.spawn import _main
import re
import sys

def is_word(dir,dict_end = {}):
    try:
        f = open(dir,"r",encoding = "utf-8")

    except Exception as e:
        print("文件打开失败：",e)
        return 0
    txt = f.read()#读取文件内容到字符串txt
    f.close() 
    set_char = set()#分隔符字符集合串的集合
    for i in set(txt):
        if not ("a" <= i <= "z" or "A" <= i <= "Z"):
            set_char.add(i)
    split_char = ""  #正则表达式分隔符字符集  
    for i in set_char:
        if i in {".","!","^","*","(",")","[","]","{","}","?","|","$","\\","'","''"}:
            split_char += "\\"+ i + "|"
        else:
            split_char  += i + "|"
    split_char = split_char[:-1]
    # print(split_char)
    set_word = re.split(split_char,txt)#分隔hot文件内容，并返回一个列表set_word

    for i in set_word:
        if i == "":
            continue
        i = i.lower()
        if i in dict_end:
            dict_end[i] += 1
        else:
            dict_end[i] = 1
    return dict_end
# print(is_word(r"D:\桌面\adfa.txt"))
if __name__ == "_main_":
    if is_word(sys.argv[1]) == 0:
        print("文件打开失败")
        exit()
    else:
        lst = sorted(is_word(sys.argv[1]).items(),key=lambda x:x[1],reverse=True)
    f = open(sys.argv[2],"w")
    for i in lst:
        f.write("%s\t%d\n"%(i[0],i[1]))
    f.close()
    



#集合增加元素：set_char.add(i)
#字符串增加元素：split_char += i 
#正则表达式分隔符字符串集：split_char = "" 
