# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/26 15:12'
__author__ = 'Remix'
import pandas as pd
from matplotlib import pyplot as plt

file_path = "E:\python\python课件\数据分析资料\day05\code\Books.csv"
df = pd.read_csv(file_path)

# print(df.head(2))
# print(df.info)
# 每年出书的数量
# data1 = df[pd.notnull(df["original_publication_year"])]
# grouped = data1.groupby(by = "original_publication_year").count()["title"]

# 不同年份书的平均评分情况
data1 = df[pd.notnull(df["original_publication_year"])]
grouped=data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()

_x=grouped.index
_y=grouped.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10],rotation=45)
plt.show()