# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/7/23 11:50'
__author__ = 'Remix'
import seaborn as sn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 加载seaborn自带数据库：iris
df=sn.load_dataset('iris')
df.head()

# swarm绘制散点以树状连接个点，不重合
# sn.swarmplot(x='species', y='petal_length', data=df, size=10)

# stripplot可以绘制分类数据的散点图，由于过多的点会聚集在一起，使用jitter进行随机抖动
sn.stripplot(x='species', y='petal_length', data=df, jitter=True)
plt.show()