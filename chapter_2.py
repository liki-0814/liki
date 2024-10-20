# 导入库
import torch

# 生成等差tensor
x = torch.arange(12)
print(f"{x}\nx的形状为：{x.shape}\nx的总数量为：{x.numel()}")

# 改变张量形状
x_reshape = x.reshape([3, 4])
print(f"\n改变后的张量：\n{x_reshape}")

# 生成全零张量
tensor_zeros = torch.zeros((2, 3, 4))
tensor_ones = torch.ones((2, 3, 4))
print(tensor_zeros, tensor_ones)

# 生成随机高斯采样张量
tensor_random = torch.randn(3, 4)
print(tensor_random)

# 转化列表为张量
tensor_changed = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(tensor_changed)
