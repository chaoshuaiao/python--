import pandas as pd

data = {
    "area" : [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    "rooms" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "price" : [100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000],
    "floor" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "location":["chaoyang","haidian","changping","fangshan","huairou","shunyi","mentougou","miyun","pinggu","xizhimenbei"],
    "year_built": [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035]

}

df = pd.DataFrame(data)

#一、数据预处理
from sklearn.model_selection import train_test_split#数据集划分
from sklearn.preprocessing import StandardScaler,OneHotEncoder#数据标准化,独热编码
from sklearn.compose import ColumnTransformer#多列转换器
from sklearn.pipeline import Pipeline #管道

#特征工程
X = df[["area","rooms","floor","location","year_built"]]
y = df["price"]

#数据集划分
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#构建管道
numeric_features = ['area','rooms','floor','year_built']#数值特征
categorical_features = ['location']#分类特征

numeric_transformer = Pipeline(steps = [('scaler', StandardScaler())])#数值特征->标准化
# 分类特征->独热编码，处理测试集中的新类别
categorical_transformer = Pipeline(steps = [('onehot', OneHotEncoder(handle_unknown='ignore'))])

#组合成多列转换器
preprocessor = ColumnTransformer(
    transformers = [
        ('num',numeric_transformer,numeric_features),
        ('cat',categorical_transformer,categorical_features)
    ] 
)

#查看数据预处理后的结构
X_train_transformed = preprocessor.fit_transform(X_train)
# print(X_train_transformed)

#二、建立模型，模型训练
from sklearn.linear_model import LinearRegression#线性回归

#建立模型,构建一个包含预处理和回归模型的管道
model_pipeline = Pipeline(steps = [('preprocessor',preprocessor),('regressor',LinearRegression())])

#模型训练
model_pipeline.fit(X_train,y_train)

#模型预测
y_pred = model_pipeline.predict(X_test)
print(y_pred)

#三、模型评估
from sklearn.metrics import mean_squared_error,r2_score#均方误差,R方

#均方误差和决定系数（R方）
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print(f"均方误差：{mse:.2f}")
print(f"R方:{r2:.2f}")

#四、模型优化
from sklearn.model_selection import GridSearchCV#网格搜索

#使用网格搜索优化模型，对线性回归的超参数进行调优（仅调整‘fit_intercept’）
parm_grid = {'regressor__fit_intercept':[True,False]}#是否拟合截距

grid_search = GridSearchCV(model_pipeline,param_grid=parm_grid,cv=5,scoring = 'neg_mean_squared_error',verbose=1)#网格搜索
grid_search.fit(X_train,y_train)

#查看最佳参数和最佳模型
print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳模型：{grid_search.best_estimator_}")

#使用最佳模型预测
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
#使用最佳模型评估的均方误差和决定系数（R方）
mse_best = mean_squared_error(y_test,y_pred_best)
r2_best = r2_score(y_test,y_pred_best)
print(f"最佳模型均方误差：{mse_best:.2f}")
print(f"最佳模型R方:{r2_best:.2f}")


