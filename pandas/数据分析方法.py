from sklearn.datasets import load_iris
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from datetime import datetime


# #sklearn库的运用
# from sklearn import preprocessing
# data = load_iris()
# df = pd.DataFrame(data.data,columns = data.feature_names,index = data.target)
# print(df.index)
# print((df.index).dtype)

# #零均值化，标准化
# zero_mean_b = (b-b.mean())/b.std()
# zero_mean_b = preprocessing.scale(b)
# Zero_Mean_b = preprocessing.StandardScaler().fit_transform(b)    #利用StandardScaler类进行零均值化，比上面方法更复杂，但更灵活通用
# #最小最大化归一化
# # minmax_b = (b-b.min())/(b.max()-b.min())
# minmax_b = preprocessing.minmax_scale(b)  
# minmax_b = preprocessing.MinMaxScaler().fit_transform(b)  #利用MinMaxScaler类进行最小最大化，比上面方法更复杂，但更灵活通用

# #离散化：等宽法
# # dis_b = pd.cut(b,bins=3,labels=['low','mid','high'])
# #等频法
# # dis_b = pd.qcut(b,q=3,labels=['low','mid','high'])


# #特征二值化
# binarizer_b = preprocessing.Binarizer(threshold=500).transform(b)

a = np.random.randint(0,10,(5,3))
b = pd.DataFrame(a,columns=['a','b','c'])
b.iloc[2,2] = np.nan

print(b)
# 处理缺失值
# print(b.loc[:,['a','b']].astype(float))
print(b[["a",'b']].apply(float))

