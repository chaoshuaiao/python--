import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt




pd.set_option('display.unicode.east_asian_width',True)

#加载鸢尾花数据集
data = load_iris()
df = pd.DataFrame(data.data,columns=data.feature_names)
df['target'] = data.target
df['species'] = df['target'].apply(lambda x:data.target_names[x])
# print(df.head())

# # 绘制特征之间的关系
# import seaborn as sns
# sns.pairplot(df, hue="species")
# plt.show()


#一、标准化
from sklearn.preprocessing import StandardScaler
x = df.drop(columns=['target','species'])
y = df['target']
scaler = StandardScaler()   
X_scaled = scaler.fit_transform(x)

#二、特征选择
from sklearn.feature_selection import SelectKBest,f_classif
# 选择前k个最好的特征
selector = SelectKBest(f_classif,k=2)
X_new = selector.fit_transform(X_scaled,y)
#打印选择的特征
selectoed_features = selector.get_support(indices=True)

#三、建立一个分类模型，使用决策树或SVM进行分类
#（1）使用决策树分类器
from sklearn.model_selection import train_test_split#划分数据集
from sklearn.tree import DecisionTreeClassifier#决策树分类器
from sklearn.metrics import accuracy_score#准确率


#划分数据集
X_train,X_test,y_train,y_test = train_test_split(X_new,y,test_size=0.2,random_state=42)
#决策树分类器
model_dt = DecisionTreeClassifier(random_state=42)
#训练模型
model_dt.fit(X_train,y_train)
#预测
y_pred_dt = model_dt.predict(X_test)
#准确率
accuracy_dt = accuracy_score(y_test,y_pred_dt)
# print(f"决策树分类器准确率：{.4f}",accuracy_dt)

# #（2）、使用SVC进行分类   
# from sklearn.model_selection import train_test_split#划分数据集
# from sklearn.svm import SVC#支持向量机分类器
# from sklearn.metrics import accuracy_score#准确率

# #划分数据集
# X_train,X_test,y_train,y_test = train_test_split(X_new,y,test_size=0.2,random_state=42)
# #初始化SVM分类器
# model_svm = SVC(kernel='linear',random_state=42)
# #训练模型
# model_svm.fit(X_train,y_train)
# #预测
# y_pred_svm = model_svm.predict(X_test)
# #准确率
# accuracy_svm = accuracy_score(y_test,y_pred_svm)
# # print("SVM分类器准确率：{accuracy_svm:.4f}")

#四、评估模型
#（1）、使用混淆矩阵评估模型
# from sklearn.metrics import confusion_matrix#混淆矩阵
# cm = confusion_matrix(y_test,y_pred_dt)
# from sklearn.metrics import classification_report#分类报告
# report = classification_report(y_test,y_pred_dt)


#（2）、使用ROC曲线评估模型,但只适用于二分类问题，因此本例中不适用
# from sklearn.metrics import roc_curve#ROC曲线
# from sklearn.metrics import auc#AUC
# fpr,tpr,thresholds = roc_curve(y_test,y_pred_dt)
# roc_auc = auc(fpr,tpr)

#调优模型：网格搜索调优

#定义决策树的参数网络
#max_depth：表示决策树的最大深度。如果设置为None，则表示树可以生长到最大深度。
#min_samples_split：表示内部节点再划分所需最小样本数。
#min_samples_leaf：表示叶子节点所需的最小样本数。
param_grid = {'max_depth':[3,5,10,None],'min_samples_split':[2,5,10],'min_samples_leaf':[1,2,4]}
#初始化模型
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV#网格搜索
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42),param_grid=param_grid,cv=5)
#训练模型
grid_search.fit(X_train,y_train)
#打印最佳参数,最佳准确率,最佳模型
# print(grid_search.best_params_,grid_search.best_score_,grid_search.best_estimator_)
#预测
y_pred_grid = grid_search.best_estimator_.predict(X_test)
#准确率
accuracy_grid = accuracy_score(y_test,y_pred_grid)
# print(f"网格搜索决策树分类器准确率：{accuracy_grid:.4f}")
   
#五、模型保存与加载
#(1)使用joblib保存模型
import joblib
#保存模型到本地
joblib.dump(grid_search.best_estimator_,'iris_model.pkl')
#加载模型
model_load = joblib.load('iris_model.pkl')

# #(2)使用pickle保存模型
# import pickle
# #保存模型到本地
# with open('iris_model.pkl','wb') as f:
#     pickle.dump(grid_search.best_estimator_,f)
# #加载模型
# with open('iris_model.pkl','rb') as f:
#     model_load = pickle.load(f)

test =pd.DataFrame([[1.4,0.2]],columns=['petal length (cm)','petal width (cm)'])
test_scaled = scaler.transform(test)#标准化
print(test_scaled)
test_new = selector.transform(test_scaled)#特征选择
print(test_new)

y_pred_test = model_load.predict(test_new)

print(y_pred_test)



