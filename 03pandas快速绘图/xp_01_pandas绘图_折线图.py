# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/7/23 10:21'
__author__ = 'Remix'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(5,3)
df = pd.DataFrame(np.abs(data),
                  index=['Mon','Tue','Wen','Thir','Fir'],
                  columns=['A','B', 'C'])
# print(df)
df.plot()
plt.show()