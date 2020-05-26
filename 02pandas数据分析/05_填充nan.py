# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/8/25 14:47'
__author__ = 'Remix'
import numpy as np

def fill_nan(t):
    for i in range(t.shape[1]):
        temp_col = t[:,i]
        nan_num = np.count_nonzero(temp_col==temp_col)
        if nan_num !=0:
            temp_not_nan_col = temp_col[temp_col==temp_col]
            temp_col[np.isnan(temp_col)]=temp_not_nan_col.mean()
    return t


if __name__=="__main__":
    t = np.arange(12).reshape(3, 4).astype("float")
    t[1, 2:] = np.nan
    print(t)
    t = fill_nan(t)
    print(t)
