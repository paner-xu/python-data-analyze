# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/24 22:53'
__author__ = 'Remix'
import numpy as np
US_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/US_video_data_numbers.csv"
GB_file = "E:/python/python课件/数据分析资料/day03/code/youtube_video_data/GB_video_data_numbers.csv"

# type表示获取数据的类型   dtype表示获取数组元素的类型   astype表示修改数据类型
t1 = np.loadtxt(US_file,delimiter=",",dtype="int")
t2 = np.loadtxt(GB_file,delimiter=",",dtype="int")

print(t1)
print("*" * 100)
print(t2)