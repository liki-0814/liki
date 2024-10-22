"""
标量、向量、矩阵、张量
"""
import torch

A = torch.arange(20).reshape((4, 5))
A_T = A.T  # 转置

X = torch.arange(24).reshape((2, 3, 4))

A = torch.arange(20, dtype=torch.float32).reshape((4, 5))
B = A.clone()

A_B_Hadamard = A * B  # Hadamard积，对应元素相乘

a = 2
# a + X  # 所有元素加上2，不改变形状

'''
X: 2,3,4
X.sum(): 1
X.sum(axis=0): 3,4
X.sum(axis=1): 2,4
X.sum(axis=2): 2,3

X.sum(axis=1, keepdim=True): 2,1,4
X.sum(axis=2, keepdim=True): 2,3,1

X.cumsum(axis=0): 指定维度逐行累加
'''

# 点积
x = torch.arange(4, dtype=torch.float32)
y = torch.ones(4, dtype=torch.float32)
# x.dot(y)  # 向量点积

'''
向量点积向量：torch.vdot()
矩阵点积向量：torch.mv()
矩阵点积矩阵：torch.mm()
'''

'''
L1范数：torch.abs().sum()
L2范数：torch.norm()
'''
