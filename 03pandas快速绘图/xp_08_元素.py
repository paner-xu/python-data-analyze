# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/7/23 8:55'
from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure(figsize=(10,5))
data = np.linspace(0,10,100)
plt.plot(data, np.sin(data), 'r-o', label ='test legend A')
plt.plot(data, np.cos(data), 'g--', label ='test legend B')
plt.xlabel('i am x axis')
plt.ylabel('i am y axis')
plt.legend()
plt.title('data desc')
plt.show()