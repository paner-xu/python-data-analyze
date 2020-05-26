# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/27 12:52'
__author__ = 'Remix'
import pandas as pd
from matplotlib import pyplot as plt
file_path="E:\python\python课件\数据分析资料\day06\code\PM2.5\BeijingPM20100101_20151231.csv"
df=pd.read_csv(file_path)

# print(df.head(2))
# print(df.info())

#把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
period=pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
df["datetime"]=period
# print(df.head(2))

# 将datetime设置为索引
df.set_index("datetime",inplace=True)
#print(type(df))

# 进行降采样
df=df.resample("7D").mean()
# print("*"*100)
# print(df.head(10))

data=df["PM_US Post"]
data_cn=df["PM_Nongzhanguan"]
#print(data)

# 画图
_x=data.index
_x_cn=data_cn.index
_y=data.values
_y_cn=data_cn.values

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y,label="PM_US Post",alpha=0.7)
plt.plot(range(len(_x_cn)),_y_cn,label="PM_Nongzhanguan",alpha=0.7)

plt.xticks(range(0,len(_x),10),list(_x)[::10],rotation=45)
plt.legend(loc="best")
plt.show()

