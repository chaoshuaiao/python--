import chardet
from typing import assert_type
from numpy import datetime_data, float64
import pandas as pd

#检测文件编码
# with open('D:\桌面\salesreport_202504.csv', 'rb') as file:
#     result = chardet.detect(file.read())
#     print(result)


#读取文件
df =   pd.read_csv(r"D:\桌面\fungoodgame\salesreport_202508.csv",encoding='utf-8')
df_huilv =  pd.read_csv("D:\桌面\常用文件\汇率.csv",encoding='utf-8')

#将汇率表中汇率导入到数据表
date =  pd.merge(df,df_huilv,on ="Currency of Sale",how="left")

#删除多余的列
date = date.drop(["Base Plan ID","Offer ID","Group ID","First USD 1M Eligible","Promotion ID"
           ,"Coupon Value","Discount Rate","Featured Product ID","Price Experiment ID"],axis=1)

#将“City of Buyer”列空值替换为“Country of Buyer”的值
date["City of Buyer"] =date["City of Buyer"].fillna(date["Country of Buyer"])


#数据整理：将未知汇率从nan转为更显眼的500
if date["汇率"].isna().any():
    print("汇率未知")
    data_nan = date[date["汇率"].isna()]
    print(data_nan["Currency of Sale"])
    date["汇率"] = date["汇率"].fillna(500)

#数据清洗：将charged amount中string不符合转float的字符去掉
date["Charged Amount"] = date["Charged Amount"].astype(str).str.replace(",","")


#将charged amount列string数据转为float数据
date["Charged Amount"]= date["Charged Amount"].astype(float)

#统计金额并生成“金额”列
date["金额"] =  date["汇率"]*date["Charged Amount"]

#产品id替换名称
try :
    date = date.replace("com.redraingame.bag","Zombie Defense Bag")
except:
    print("com.redraingame.bag不存在")
try :
    date = date.replace("com.fungoodgames.sg","Dynasty Squad")
except:
    print("com.fungoodgames.sg不存在")

date_pivot =    pd.pivot_table(date,index ="Order Charged Date",columns ="Product ID",
                            values={"金额","City of Buyer"},aggfunc={"金额":"sum","City of Buyer":"nunique"},margins= False)
#利用ExcelWriter类将两个表格数据写入同一个excel文件
with pd.ExcelWriter(r"D:\桌面\fungoodgame\salesreport_202508_改.xlsx",engine='openpyxl') as wrter:
    date_pivot.to_excel(wrter,sheet_name='透视表')
    date.to_excel(wrter,sheet_name='原数据')
print("操作已完成：")
# date_pivot_2 =  date_pivot.pivot(index="Order Charged Date",columns=["com.OneTwo.TD","com.onicore.backpack.rush"],values="All")
# print(date_pivot_2)
# date.to_excel(r"D:\桌面\fungoodgame\salesreport_202507_改.xlsx")
# date_pivot.to_excel(r"D:\桌面\fungoodgame\salesreport_202507_透视表.xlsx")
# print("操作已完成：")

