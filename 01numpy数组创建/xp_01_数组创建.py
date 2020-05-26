# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/4/8 18:24'
__author__ = 'Remix'
# 调用numpy包
import numpy as np
import random
# 使用array-range创建数组
t1 = np.array(range(1,5))
# 输出数组和数组类型
print(t1)
print(type(t1))
# 使用arange创建数组
t2 = np.arange(5)
print(t2)
print(type(t2))

t3 = np.array([4,10,2])
print(t3)
# 存储的数据类型
print(t3.dtype)

t4 = np.array(range(1,4),dtype = float)
print(t4)
print(t4.dtype)
t5 = np.array(range(4,8),dtype = "float32")
print(t5)
print(t5.dtype)

# bool类型
t6 = np.array([1,1,0,1,0], dtype=bool)
print(t6)
print(t6.dtype)

# 调整数据类型
t7 = t6.astype("int8")
print(t7)
print(t7.dtype)

# numpy中的小数
t8 = np.array([random.random() for i in range(10)])
print(t8)
print(t8.dtype)
# round取小数，t8保留两位小数
t9 = np.round(t8,2)
print(t9)