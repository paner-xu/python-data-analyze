# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/25 22:10'
__author__ = 'Remix'
import pandas as pd

df = pd.read_csv("E:\python\python课件\数据分析资料\day04\code\dogNames2.csv")
# sort默认情况下升序排列
df = df.sort_values("Count_AnimalName")
# ascending=False降序排列
df = df.sort_values("Count_AnimalName",ascending=False)
print(df.head(5))
print(df.info())
print("*"*100)
# 计算数值
print(df.describe())

# dataframe索引
# -方括号里面写数字，表示取行，对行进行操作
# -方括号里面写字符串，表示取列，对列进行操作
print(df[:20]["Count_AnimalName"])
print(df["Count_AnimalName"])
print(type(df["Count_AnimalName"]))
