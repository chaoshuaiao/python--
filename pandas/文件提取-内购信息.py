
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np

# print(help(pd.to_datetime))


with open(r"D:\桌面\内购.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

# 去除行末的换行符
data = [line.strip() for line in data]

# 初始化列表来存储整理后的数据
organized_data = {'内购名称': [], '内购id': [], '金额': [], '原文': []}

# 定义分隔符
delimiter = ','
line_num = 0
# 遍历每一行数据
for line in data:
    # 使用find方法找到分隔符的位置
    first_comma = line.find(delimiter)
    second_comma = line.find(delimiter, first_comma + 1)
    
    if first_comma != -1 and second_comma != -1:
        # 提取内购名称、内购id和金额
        内购名称 = line[:first_comma]
        内购id = line[first_comma + 1:second_comma]
        金额 = line[second_comma + 1:]
        
        # 将提取的数据添加到列表中
        organized_data['内购名称'].append(内购名称)
        organized_data['内购id'].append(内购id)
        organized_data['金额'].append(金额)
        organized_data['原文'].append(line)
        line_num += 1
    else:
        # 处理格式不正确的行
        print(f"格式不正确的行: {line_num + 1 }")

# 将整理后的数据转换为DataFrame
df = pd.DataFrame(organized_data)

# 打印整理后的数据
# print(df)

# 如果需要将整理后的数据保存为新的Excel文件
output_file_path = r"D:\桌面\内购整理1.xlsx"
df.to_excel(output_file_path, index=False)
print(f"数据已整理并保存为 {output_file_path}")
