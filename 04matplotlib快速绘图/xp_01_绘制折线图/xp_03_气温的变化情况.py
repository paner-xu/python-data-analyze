
# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 11:31'
__author__ = 'Remix'
from matplotlib import pyplot as plt
import random
plt.rcParams['font.sans-serif']=['SimHei']  #显示中文
x = range(0,120)
y = [random.randint(20,35)for i in range(120)]

# 设置图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.plot(x,y)

# 调整x轴刻度
_xtick_label = ["10点{}分".format(i) for i in range(60)]
_xtick_label += ["11点{}分".format(i-60) for i in range(60,120)]
plt.xticks(list(x)[::3],_xtick_label,rotation = 45)  # rotation倾斜45度

# 保存图片
plt.savefig("./f1.png")

# 展示图片
plt.show()