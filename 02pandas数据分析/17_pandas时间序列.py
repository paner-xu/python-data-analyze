# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/26 16:38'
__author__ = 'Remix'
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "E:\python\python课件\数据分析资料\day06\code\911.csv"
df = pd.read_csv(file_path)

# print(df.head(10))
# print(df.info())

# 获取类别
data1 = df["title"].str.split(":").tolist()
cate_list = list(set([i[0] for i in data1]))
print(cate_list)

# 构建全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
for cate in cate_list:
    zero_df[cate][df["title"].str.contains(cate)]=1

sum_ret = zero_df.sum(axis=0)
print(sum_ret)
