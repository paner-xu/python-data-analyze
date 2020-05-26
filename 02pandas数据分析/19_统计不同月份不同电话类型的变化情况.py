# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/10/26 19:37'
__author__ = 'Remix'
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "E:\python\python课件\数据分析资料\day06\code\911.csv"
df = pd.read_csv(file_path)

# 把时间字符串转换为时间类型，并设置为索引
df["timeStamp"]=pd.to_datetime(df["timeStamp"])


# 获取类别
data1 = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in data1]
df["cate"]=pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

df.set_index("timeStamp",inplace=True)

plt.figure(figsize=(20,8),dpi=80)

for group_cate, group_data in df.groupby(by="cate"):
    #对不同的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]

    _x=count_by_month.index
    _y=count_by_month.values

    _x=[i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)),_y,label=group_cate)

plt.xticks(range(len(_x)),_x,rotation=45)
plt.legend(loc="best")
plt.show()

