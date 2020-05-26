# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 16:06'
__author__ = 'Remix'
from matplotlib import pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,21,22,22,22,24,24,25]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,10,9,11,8]

x_3 = range(1,32)
x_10 = range(51,82)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图形
plt.scatter(x_3,y_3,label = "3月份")
plt.scatter(x_10,y_10,label = "10月份")


#调整刻度
_x = list(x_3) +list(x_10)
_x_ticks_label = ["3月{}日".format(i) for i in x_3]
_x_ticks_label += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_x_ticks_label[::3],rotation = 45)

# 添加图形信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("3月份和10月份温度变化情况")

# 显示图例
plt.legend(loc = "upper center")
# 添加网格
plt.grid(alpha = 0.5)

# 保存图片
plt.savefig("./f5.png")

# 展示图形
plt.show()