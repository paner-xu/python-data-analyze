# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/8 21:27'
__author__ = 'Remix'
import numpy as np
t1 = np.loadtxt("./youtube_video_data/GB_video_data_numbers.csv",
                delimiter=",",dtype=int)
print(t1)
print("-"*50)

# 取行
print(t1[1])
print("-"*50)
# 取连续多行
print(t1[2:4])
print("-"*50)
# 取不连续行
print(t1[[2,4,5]])
print("-"*50)

# 取行或列(逗号前面是行，逗号后面是列)
print(t1[1,])
print(t1[1:,])
print(t1[[2,10,3],])
print("-"*50)
# 取列
print(t1[:,0])
# 取连续的多列
print(t1[:,0:2])
# 取不连续的多列
print(t1[:,[1,3]])
print("-"*50)
# 取行和列，取第三行第四列的值
a = t1[2,3]
print(a)
# 取多行和多列，取第三行到第五行和第二列到第四列的结果
# 取得是行和列交叉点的位置
print(t1[2:5,1:4])
# 取多个不相邻的点
# 表示取（0,0），（2,2），（3,1）
print(t1[[0,2,3],[0,2,1]])


