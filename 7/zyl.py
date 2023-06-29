import pandas as pd
import numpy as np
import math

# 加载数据集
data = pd.read_csv('zoo.csv', header=None)

# 定义拉普拉斯机制函数
def laplace_mech(data, epsilon):
    sensitivity = 1  # 敏感度为1，即每个动物的消耗量
    beta = sensitivity / epsilon
    noise = np.random.laplace(0, beta, len(data))
    return data + noise

# 对每个动物的消耗量进行加噪
epsilon = 0.1
data_noisy = laplace_mech(data[1], epsilon)

# 计算每日进食超过55根胡萝卜的动物数量的近似值
count = sum(data_noisy > 55)

# 差分隐私方案设计
def diff_privacy(data, epsilon):
    sensitivity = 1  # 敏感度为1，即每个动物的消耗量
    beta = sensitivity / epsilon
    data_noisy = data + np.random.laplace(0, beta, len(data))
    return data_noisy

# 对数据集进行微小扰动，支持查询次数为20次
epsilon = 0.1
for i in range(20):
    data_noisy = diff_privacy(data[1], epsilon)
    count = sum(data_noisy > 55)
    print("第{}次查询结果：{}".format(i+1, count))

# 评估隐私保护的效果
epsilon = 0.1
data_noisy = laplace_mech(data[1], epsilon)
count_noisy = sum(data_noisy > 55)
count_true = sum(data[1] > 55)
error = abs(count_noisy - count_true) / count_true
print("隐私保护效果评估：加噪后的近似值与真实值之间的误差为{}".format(error))