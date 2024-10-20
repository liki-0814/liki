"""
-*-conding:utf-8-*-
user: lik030814@gmail.com
final changed time: 2024.10.20
"""

# 导入库
import os
import torch
import pandas as pd

'''
os.mkdir()创建路径中的最后一级目录
os.makedirs()创建多层目录
'''
os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRoom,Alley,Price\n')
    f.write('NA,Pave,127500\n')
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

# 数据读取
data = pd.read_csv(data_file)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs[:] = inputs.fillna(inputs.mean(numeric_only=True))

# 使用 pd.get_dummies() 将输入数据中的分类变量转换为虚拟变量，dummy_na=True 表示将缺失值也视为一个类别
inputs[:] = pd.get_dummies(inputs[:], dummy_na=True)

