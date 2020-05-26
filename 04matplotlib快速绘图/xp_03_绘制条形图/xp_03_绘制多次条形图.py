# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 18:54'
__author__ = 'Remix'
from matplotlib import pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 传入数据
a = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_14 = [2358,399,2358,362]
b_15 = [12357,126,2045,168]
b_16 = [15746,312,4497,319]
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

bar_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

# 绘制图形
plt.bar(range(len(a)),b_14, width = bar_width, label = "14日")
plt.bar(x_15, b_15, width = bar_width, label = "15日")
plt.bar(x_16, b_16, width = bar_width, label = "16日")

# 调整刻度
plt.xticks(x_15, a)  # 将x_15与a中的电影名对应，让其居于正中间

# 显示图例
plt.legend(loc = "upper right")

# 保存图形
plt.savefig("./f7.png")
# 展示图形
plt.show()