# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/23 19:28'
__author__ = 'Remix'
import pandas as pd

file_path = 'E:\python\python课件\数据分析资料\day04\code\IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)
print(df.info())

# 计算电影的平均分
rating_mean = df['Rating'].mean()
print(rating_mean)
# 统计演员人数
# tolist将数组转化成列表
temp_actor_list = df["Actors"].str.split(',').tolist()
actor_list = [i for j in temp_actor_list for i in j]
print(actor_list)
