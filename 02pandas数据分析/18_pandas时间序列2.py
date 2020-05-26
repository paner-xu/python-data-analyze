# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/26 18:59'
__author__ = 'Remix'
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "E:\python\python课件\数据分析资料\day06\code\911.csv"
df = pd.read_csv(file_path)

# print(df.head())
# print(df.info())


# 把时间字符串转换为时间类型，并设置为索引
df["timeStamp"]=pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp",inplace=True)

#统计出911数据中不同月份电话次数
count_of_mon=df.resample("M").count()["title"]
print(count_of_mon)

# 画图
_x=count_of_mon.index
_y=count_of_mon.values

_x=[i.strftime("%Y%m%d") for i in _x]     # 截取时间中的年月日
plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x, rotation=45)

plt.show()

