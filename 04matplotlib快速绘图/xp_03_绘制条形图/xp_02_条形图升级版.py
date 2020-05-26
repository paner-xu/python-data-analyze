# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/2 18:37'
__author__ = 'Remix'
from matplotlib import pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 传入数据
a = {"战狼2", "速度与激情8", "功夫瑜伽", "西游伏魔篇",
     "变形金刚5：最后的骑士", "加勒比海盗5：死无对证", "摔跤吧爸爸",
     "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章", "乘风破浪",
     "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战",
     "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "新木乃伊", "情圣"}
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,
     11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 用barh绘制条形图
plt.barh(range(len(a)), b, height = 0.6, color = "cyan")

# 调整坐标刻度
plt.yticks(range(len(a)), a)

# 添加图例信息
plt.ylabel("片名")
plt.xlabel("票房 单位（亿）")
plt.title("2017年排名前20的电影票房")

# 设置网格
plt.grid(alpha = 0.5, linestyle = "-.")
# 保存图形
plt.savefig("./f6.png")

#展示图形
plt.show()