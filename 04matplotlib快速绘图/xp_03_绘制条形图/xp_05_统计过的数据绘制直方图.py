# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 20:46'
__author__ = 'Remix'
from matplotlib import pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 传入数据
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图形
plt.bar(range(12), quantity, width=1)
plt.grid()
plt.savefig("./f9.png")
# 调整x刻度
_x = [i-0.5 for i in range(13)]
_xticks_labels = interval+[150]
plt.xticks(_x,_xticks_labels)
# 展示图形
plt.show()