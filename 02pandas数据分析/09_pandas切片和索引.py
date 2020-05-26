# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/9/5 16:26'
__author__ = 'Remix'
import pandas as pd
df = pd.read_csv("E:\python\python课件\数据分析资料\day04\code\dogNames2.csv")
print(df[(800<df["Count_AnimalName"])&(df["Count_AnimalName"]<1000)])  # 并
print(df[(800<df["Count_AnimalName"])|(df["Count_AnimalName"]<1000)])  # 或