# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/25 9:32'
__author__ = 'Remix'
import numpy as np

US_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/US_video_data_numbers.csv"
GB_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/GB_video_data_numbers.csv"

t1=np.loadtxt(US_file,delimiter=",",dtype="int")
t2=np.loadtxt(GB_file,delimiter=",",dtype="int")

print(t1)
print("-" * 100)
# 取行
# print(t1[0])

# 取多行
# print(t1[0:3])

# 取指定行，第二行、第五行、第八行
# print(t1[[1,4,7]])

# 取列
# print(t1[:,1])

# 取连续多列
# print(t1[:,0:3])

# 取不连续多列，第一列，第三列，第四列
# print(t1[:,[0,2,3]])

# 取点
# print(t1[[1],[1]])
# 取不相邻的点
print(t1[[0,2],[1,2]])