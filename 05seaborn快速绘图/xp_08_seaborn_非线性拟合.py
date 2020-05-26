# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/7/23 12:15'
__author__ = 'Remix'
import seaborn as sn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 加载seaborn自带数据库：iris
df=sn.load_dataset('iris')
df.head()

# order代表用二次多项式进行拟合
sn.regplot(x='sepal_length', y='petal_length', order=2, data=df)
plt.show()