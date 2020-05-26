# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/24 13:51'
__author__ = 'Remix'
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = 'E:\python\python课件\数据分析资料\day04\code\IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(3))

temp_list = df["Genre"].str.split(",").tolist()  #[[],[],[]]
print(temp_list)
#genre_list = [i for j in temp_list for i in j]
genre_list = list(set([i for j in temp_list for i in j]))

#print(genre_list)
# 构建全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns = genre_list)
# 给每部电影分类的位置设置为1
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]]=1
print(zeros_df)

# 统计每个类别电影的数量
genre_count = zeros_df.sum(axis=0)
#print(genre_count)

genre_count=genre_count.sort_values()

_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(20,8),dpi=80)

plt.bar(_x,_y, width=0.6,color="orange")
plt.xticks(rotation=45)
plt.show()