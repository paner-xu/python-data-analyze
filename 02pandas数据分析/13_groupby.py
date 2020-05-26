# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/24 18:31'
__author__ = 'Remix'
import pandas as pd
import numpy as np

file_path = "E:\python\python课件\数据分析资料\day05\code\starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
# grouped = df.groupby("Country")
# print(grouped)

# DataFrameGroupBy
# 可以遍历
#for i,j in grouped:
    #print(i)
    #print("-"*100)
    #print(j)
    #print("*" * 100)

#调用聚合方法
# 统计美国和中国星巴克门店数量
#count_brand = grouped["Brand"].count()
#print(count_brand["US"])
#print(count_brand["CN"])

#统计中国各省份星巴克门店数量
#china_data = df[df["Country"]=="CN"]
#grouped = df.groupby(by="State/Province").count()["Brand"]
#print(grouped)


# 数据按照多个条件进行分组, Series类型
#grouped = df.groupby(by=[df["Country"],df["State/Province"]]).count()["Brand"]
#print(grouped)
#print(type(grouped))

# 数据按照多个条件进行分组, DataFrame类型
grouped1 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
# grouped2 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
# grouped3 = df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()

# print(grouped1)
# print(type(grouped1))
# print("-"*100)

# print(grouped2)
# print(type(grouped2))
# print("-"*100)

# print(grouped3)
# print(type(grouped3))

# 索引的方法和属性
print(grouped1.index)