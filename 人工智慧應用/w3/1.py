import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math


SAMPLES = 1000
SEED = 1337
np.random.seed(SEED)
tf.random.set_seed(SEED)
# 產生範圍為 0 到 2pi 且均勻分布的隨機數字 , 這些數字涵蓋完整的 sin 波震盪
x_values = np.random.uniform(low=0, high=2 * math.pi, size=SAMPLES)
np.random.shuffle(x_values)  # 再次洗亂
y_values = np.sin(x_values)  # 計算對應的 sin 值
plt.plot(x_values, y_values, "b.")  # b. 表示印藍色點
plt.show()
