# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/25 16:15'
__author__ = 'Remix'
import numpy as np
from matplotlib import pyplot as plt
# US_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/US_video_data_numbers.csv"
GB_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/GB_video_data_numbers.csv"

# t1=np.loadtxt(US_file,delimiter=",",dtype="int")
t2=np.loadtxt(GB_file,delimiter=",",dtype="int")

t2 = t2[t2[:,1]<500000]
GB_comment = t2[:,-1]
GB_like = t2[:,1]

plt.figure(figsize=(20,8),dpi=80)

plt.scatter(GB_comment,GB_like)

plt.show()