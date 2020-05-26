# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/26 14:52'
__author__ = 'Remix'
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

file_path = "E:\python\python课件\数据分析资料\day05\code\starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
df = df[df["Country"]=="CN"]

data1=df.groupby(by="City")["Brand"].count().sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values
plt.figure(figsize=(20,12), dpi=80)
plt.barh(range(len(_x)),_y,height = 0.4)
plt.yticks(range(len(_x)),_x)
plt.show()