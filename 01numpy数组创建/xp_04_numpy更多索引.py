# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/9 12:15'
__author__ = 'Remix'
import numpy as np
t1 = np.arange(24).reshape((4,6))
print(t1)
# 取t1中小于11的数
print(t1[t1<11])
# 将t1中小于11的数改为3
t1[t1<11] = 3
print(t1)

# 使用where来替换数值
# 将t1中大于3的数换成2，否则为10
# t1 = np.where(t1>3,2,10)
# print(t1)
# numpy中的clip裁剪索引
# 将t1中小于11的数值改为11，将大于18的数值改为18
t2 = t1.clip(11,18)
print(t2)