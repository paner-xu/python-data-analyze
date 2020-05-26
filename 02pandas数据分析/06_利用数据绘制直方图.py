# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/25 15:52'
__author__ = 'Remix'
import numpy as np
from matplotlib import pyplot as plt
US_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/US_video_data_numbers.csv"
# GB_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/GB_video_data_numbers.csv"

t1=np.loadtxt(US_file,delimiter=",",dtype="int")
# t2=np.loadtxt(GB_file,delimiter=",",dtype="int")
US_comments = t1[:,-1]
US_comments=US_comments[US_comments<5000]

print(US_comments.max(), US_comments.min())
# 组数
d = 50
# 计算组距
bin_num = (US_comments.max() - US_comments.min())//d

plt.figure(figsize=(20,8),dpi=80)
plt.hist(US_comments,bin_num)

plt.show()

