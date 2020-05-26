# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 14:14'
__author__ = 'Remix'
from matplotlib import pyplot as plt

x = range(11,31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

# 设置图形大小
plt.figure(figsize=(20,8), dpi=80)

plt.rcParams['font.sans-serif']=['SimHei']
# 添加图形基本信息
plt.xlabel("岁数")
plt.ylabel("男女朋友 单位（个）")
plt.title("11岁到30岁每年交往男女朋友的数量情况")

# 调整x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,rotation = 45)

# 增加网格
plt.grid()

# 保存图形
plt.savefig("./f3.png")

#绘制图形
plt.plot(x,y)

#展示图形
plt.show()