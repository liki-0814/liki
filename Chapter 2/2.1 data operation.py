"""
-*-conding:utf-8-*-
user: lik030814@gmail.com
final changed time: 2024.10.20
"""

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
tensor_changed = torch.tensor([[1, 2, 3, 4],
                               [5, 6, 7, 8],
                               [9, 10, 11, 12]])
print(tensor_changed)

# operation
tensor_1 = torch.tensor([1.0, 2, 4, 8])
tensor_2 = torch.tensor([2, 2, 2, 2])

print("\nAddition: \n", tensor_1 + tensor_2)
print("\nSubtraction: \n", tensor_1 - tensor_2)
print("\nMultiplication: \n", tensor_1 * tensor_2)
print("\nDivision: \n", tensor_1 / tensor_2)
print("\nPower Operation: \n", tensor_1 ** tensor_2)
print("\nEuler's number: \n", torch.exp(tensor_1))

tensor_3 = torch.tensor([[1, 2, 4, 8],
                         [1, 2, 4, 8]])
tensor_4 = torch.tensor([[2, 2, 2, 2],
                         [2, 2, 2, 2]])
print("\nConcatenate on row: \n{}\nConcatenate on column: \n{}"
      .format(torch.cat((tensor_3, tensor_4), dim=0),
              torch.cat((tensor_3, tensor_4), dim=1)))

print("\nBool Operation: \n", tensor_3 == tensor_4)

print("\nSum: \n", torch.sum(tensor_3))

# broadcast
tensor_5 = torch.arange(3)
tensor_6 = torch.arange(2)

tensor_5_broadcast = tensor_5.reshape((3, 1))
tensor_6_broadcast = tensor_6.reshape((1, 2))

print(
    "\ntensor_5: \n{}\nbroadcast: \n{}\n"
    "\ntensor_6: \n{}\nbroadcast: \n{}"
    .format(tensor_5, tensor_5_broadcast,
            tensor_6, tensor_6_broadcast))
print(tensor_5_broadcast + tensor_6_broadcast)

# Indexing and slicing
tensor_7 = torch.arange(12, dtype=torch.float32).reshape((3, 4))
print("\ntensor_7: \n", tensor_7)
print("\ntensor_7[-1]: \n", tensor_7[-1])
print("\ntensor_7[1:3]: \n", tensor_7[1:3])

# insert and change
tensor_7[1, 2] = 9
print("\ntensor_7_changed_v1: \n", tensor_7)

tensor_7[0:2] = 12
print("\ntensor_7_changed_v2: \n", tensor_7)

# Save memory
tensor_8 = torch.tensor([[2.0, 1, 4, 3],
                         [1, 2, 3, 4],
                         [4, 3, 2, 1]])
tensor_8_id_before = id(tensor_8)
tensor_8 = tensor_8 + tensor_7
tensor_8_id_after = id(tensor_8)
print("id:\n{}\n{}\n{}".format(tensor_8_id_before, tensor_8_id_after, tensor_8_id_before == tensor_8_id_after))

tensor_9 = torch.zeros_like(tensor_8)
tensor_9_id_before = id(tensor_9)
tensor_9[:] = tensor_8 + tensor_7
tensor_9_id_after = id(tensor_9)
print("id:\n{}\n{}\n{}".format(tensor_9_id_before, tensor_9_id_after, tensor_9_id_before == tensor_9_id_after))

# Change character type
numpy_10 = tensor_7.numpy()
tensor_11 = torch.tensor(numpy_10)
print("numpy_10_type: ", type(numpy_10))
print("tensor_11_type: ", type(tensor_11))
