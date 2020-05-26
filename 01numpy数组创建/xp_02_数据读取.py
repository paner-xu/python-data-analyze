# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/8 19:28'
__author__ = 'Remix'
import numpy as np
t1 = np.loadtxt("./youtube_video_data/GB_video_data_numbers.csv",
                delimiter=",",dtype=int)
print(t1)
print("-"*50)
# 数据的转置
# 方法一
t2 = np.loadtxt("./youtube_video_data/GB_video_data_numbers.csv",
                delimiter=",",dtype=int,unpack=True)
print(t2)
print("-"*50)
# 方法二
t3 = t2.T
print(t3)
print("-"*50)
# 方法三
t4 = t3.transpose()
print(t4)
print("-"*50)
# 方法四
t5 = t4.swapaxes(1,0)
print(t5)