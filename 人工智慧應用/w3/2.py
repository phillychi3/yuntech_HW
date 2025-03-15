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
TRAIN_SPLIT=int(0.6*SAMPLES)
TEST_SPLIT=int(0.2*SAMPLES+TRAIN_SPLIT)
x_train, x_validate, x_test = np.split(x_values, [TRAIN_SPLIT, TEST_SPLIT])
y_train, y_validate, y_test = np.split(y_values, [TRAIN_SPLIT, TEST_SPLIT])
# 確認加起來可以得到完整大小
assert(x_train.size+x_validate.size+x_test.size)==SAMPLES
# 繪圖
plt.plot(x_train, y_train, 'b.', label="Train")
plt.plot(x_validate, y_validate, 'y.', label="Validate")
plt.plot(x_test, y_test, 'r.', label="Test")
plt.legend()
plt.show()