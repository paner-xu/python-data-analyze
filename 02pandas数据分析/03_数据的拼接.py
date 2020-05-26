# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/25 10:39'
__author__ = 'Remix'
import numpy as np
# 加载国家数据
US_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/US_video_data_numbers.csv"
GB_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/GB_video_data_numbers.csv"

t1 = np.loadtxt(US_file,delimiter=",",dtype="int")
t2 = np.loadtxt(GB_file,delimiter=",",dtype="int")

# 添加国家信息
zero_data = np.zeros((t1.shape[0],1)).astype(int)
one_data = np.ones((t2.shape[0],1)).astype(int)

# 拼接
US_data = np.hstack((t1,zero_data))
GB_data = np.hstack((t2,one_data))

final_data = np.vstack((US_data,GB_data))

print(final_data)