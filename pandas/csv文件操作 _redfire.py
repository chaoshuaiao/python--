import chardet
from typing import assert_type
from numpy import datetime_data, float64
import pandas as pd

#检测文件编码
# with open('D:\桌面\salesreport_202504.csv', 'rb') as file:
#     result = chardet.detect(file.read())
#     print(result)


#读取文件
df =   pd.read_csv(r"D:\桌面\redfire\salesreport_202508.csv",encoding='utf-8')
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

# print(date.iloc[int(date.shape[0]),int(date.shape[1])-1])

#数据清洗：将charged amount中string不符合转float的字符去掉
date["Charged Amount"] = date["Charged Amount"].astype(str).str.replace(",", "")
date["Charged Amount"] = pd.to_numeric(date["Charged Amount"])
# date["Charged Amount"] = date["Charged Amount"].astype(str).apply(lambda x: eval(x.replace(",", "")) if x.replace(",", "").replace('.', '', 1).replace('-', '', 1).isdigit() else 0)


#统计金额并生成“金额”列
date["金额"] =  date["汇率"]*date["Charged Amount"]

try :
    date = date.replace("com.red.fire.candybombmatch","Candy Bomb Match")
except:
    print("com.redraingame.bag不存在")

date_pivot =  pd.pivot_table(date,index ="Order Charged Date",columns ="Product ID",
                               values=["金额","City of Buyer"],aggfunc={"金额":"sum","City of Buyer":"nunique"},margins= False)

# date_pivot_2 =  date_pivot.pivot(index="Order Charged Date",columns=["com.OneTwo.TD","com.onicore.backpack.rush"],values="All")
# print(date_pivot_2)
with pd.ExcelWriter(r"D:\桌面\redfire\salesreport_202508_改.xlsx")as write:

    date_pivot.to_excel(write,sheet_name="透视表")
    date.to_excel(write,sheet_name="原数据")


print("操作已完成：")

