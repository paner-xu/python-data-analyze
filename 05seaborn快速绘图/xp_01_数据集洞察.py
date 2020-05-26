# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/7/23 11:36'
__author__ = 'Remix'
import seaborn as sn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 加载seaborn自带数据库：iris
df=sn.load_dataset('iris')
df.head()

# 基本统计信息
des= df.describe()
print(des)
