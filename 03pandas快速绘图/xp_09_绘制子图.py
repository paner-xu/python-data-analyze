# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/7/23 9:16'
__author__ = 'Remix'
from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure(figsize=(10,5))
data = np.linspace(0,10,100)

#每一个子图是独立的，如是否显示图例，需要单独在子图函数下面增加
plt.subplot(3,2,1)
plt.plot(data, np.sin(data), 'r', label='test legend 1')
plt.legend()

plt.subplot(3,2,2)
plt.plot(data, np.cos(data), 'g', label='test legend 2')
plt.legend()

plt.subplot(3,2,3)
plt.plot(data, np.cos(data), 'c', label='test legend 3')
plt.legend()

plt.subplot(3,2,4)
plt.plot(data, np.cos(data), 'm', label='test legend 4')
plt.legend()

plt.subplot(3,2,5)
plt.plot(data, np.cos(data), 'y', label='test legend 5')
plt.legend()

plt.subplot(3,2,6)
plt.plot(data, np.cos(data), 'k', label='test legend 6')
plt.legend()

# plt.subplot(3,2,6)
# plt.plot(data, np.cos(data), 'k_', label='test legend 666')
# plt.legend()
plt.subplot(3,1,3)
plt.plot(data, np.cos(data), 'k_', label='test legend 888')
plt.legend()

plt.show()

