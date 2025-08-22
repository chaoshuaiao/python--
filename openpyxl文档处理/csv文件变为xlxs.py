import csv
from gettext import find
from locale import getencoding
import traceback
import chardet

# with open(r"D:\桌面\text1.csv","w",encoding="gbk") as f:
#     writ =  csv.writer(f)
#     writ.writerow(['姓名','年龄'])
#     writ.writerow(["jlkjkl","d"])

# with open(r"D:\桌面\salesreport_202408.csv","r",encoding="gbk") as f:
#     read =  csv.reader(f)
#     for i in read:
#         print(i)


with open(r"D:\桌面\salesreport_202408.csv","r",encoding=  "ascii") as f:
    read =  csv.reader(f)
    n = 1
    for i in read:
        if n < 5:
            n += 1
            print(read)
#     print("捕获到异常: {}".format(zero))



#获取文件的encoding编码
# with open(r"D:\桌面\salesreport_202408.csv","rb") as f:
#     read =  f.read(3)
#     encode_read = chardet.detect(read)["encoding"]
#     print("尝试运行代码: {}".format(encode_read))

