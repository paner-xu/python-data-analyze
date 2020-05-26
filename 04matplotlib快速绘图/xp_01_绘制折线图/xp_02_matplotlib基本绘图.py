# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 11:13'
__author__ = 'Remix'
from matplotlib import pyplot as plt
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

# 设置图片大小
plt.figure(figsize=(20,8),dpi=80)

# 设置坐标轴刻度
plt.xticks(range(2,26))  #每隔一个刻度取一个
plt.yticks(range(min(y),max(y)+1))  #y的取值在其最大值与最小值之间

# 绘图
plt.plot(x,y)

# 保存图片
plt.savefig("./fi.png")

# 展示图片
plt.show()