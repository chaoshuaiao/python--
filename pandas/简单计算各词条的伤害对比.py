import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#星见雅配置
class ya():
     # 佩戴专武后攻击力
    Attack = 880 + 743 + 316 
    # 暴击率：本身+专武+二命15暴击+磁盘四件套
    Critical = 0.05 + 0.24 + 0.15 + 0.12  
    # 爆伤：本身+专武+4号磁盘+磁盘四件套
    Critical_damage = 0.5 + 0.5 + 0.48 + 0.46  
    #穿透率
    Penetration = 0.36
    #穿透值
    Penttration_value = 0.0
    #精通
    Control = 238
    #增伤:核心被动普攻60增伤+专武两层40
    Increased_injury = 0.6+0.4



#初始化模板
ya_data = np.array([ya.Attack,ya.Critical,ya.Critical_damage,ya.Penttration_value,ya.Control,ya.Increased_injury],dtype=float)
data = pd.DataFrame(ya_data,index=['攻击力','暴击率','暴击伤害','穿透值','精通','增伤'])  
data = data.T
# print(data)



#每攻击力词条伤害提升
def Improve():
    i = 1
    while i < 101:

        #每攻击力词条伤害提升
        Attack_new = ya.Attack*(1.3+i*0.03)
        data.loc[i,"攻击力UP"] = Attack_new * 794/((954*(1-0.36) *(1-ya.Penetration)-ya.Penttration_value)+794) * (1+ya.Increased_injury) *(1+ya.Critical_damage * ya.Critical)*(1+0.3)
        #每暴击率词条伤害提升
        Critical_new = ya.Critical + i*0.024
        if Critical_new > 1:
            Critical_new = 1
        data.loc[i,"暴击率UP"] = ya.Attack * 794/((954*(1-0.36) *(1-ya.Penetration)-ya.Penttration_value)+794) * (1+ya.Increased_injury) *(1+ya.Critical_damage * Critical_new)*(1+0.3)
        #每暴击伤害词条伤害提升
        Critical_damage_new = ya.Critical_damage + i*0.048
        data.loc[i,"暴击伤害UP"] = ya.Attack * 794/((954*(1-0.36) *(1-ya.Penetration)-ya.Penttration_value)+794) * (1+ya.Increased_injury) *(1+Critical_damage_new * ya.Critical)*(1+0.3)
        #每穿透值词条伤害提升
        Penttration_value_new = ya.Penttration_value + i*9
        data.loc[i,"穿透值UP"] = ya.Attack * 794/((954*(1-0.36) *(1-ya.Penetration)-Penttration_value_new)+794) * (1+ya.Increased_injury) *(1+ya.Critical_damage * ya.Critical)*(1+0.3)
        # #每精通词条伤害提升
        # Control_new = ya.Control + i*10
        # data.loc[i,"精通UP"] = ya.Attack * 794/((954*(1-0.36) *(1-ya.Penetration)-ya.Penttration_value)+794) * (1+ya.Increased_injury) *(1+ya.Critical_damage * ya.Critical)*(1+0.3)
        #每增伤词条伤害提升
        Increased_injury_new = ya.Increased_injury + i*0.1
        data.loc[i,"增伤UP"] = ya.Attack * 794/((954*(1-0.36) *(1-ya.Penetration)-ya.Penttration_value)+794) * (1+Increased_injury_new) *(1+ya.Critical_damage * ya.Critical)*(1+0.3)   
        i += 1
Improve()
#去除无效数据
data = data.drop(0)
data = data.dropna(how='all',axis=1)
non =  np.array(data).astype(int)
indi = np.arange(1,101).reshape(100,1)

non = np.concatenate((indi,non),axis=1)

data = pd.DataFrame(non,columns=['词条','攻击力UP','暴击率UP','暴击伤害UP','穿透值UP','增伤UP'])  
print(data)
# print(data)
# plt字体设置
x=data["词条"]
y1=data["攻击力UP"]
plt.plot(x,y1,label='攻击力')
y2=data["暴击率UP"]
plt.plot(x,y2,label='暴击率')
y3=data["暴击伤害UP"]
plt.plot(x,y3,label='暴击伤害')
y4=data["穿透值UP"]
plt.plot(x,y4,label='穿透值')
y5=data["增伤UP"]
plt.plot(x,y5,label='增伤')
plt.title("各词条伤害提升")
plt.xlabel("词条")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

plt.legend()
plt.show()  
