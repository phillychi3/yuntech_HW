import numpy as np
import matplotlib.pyplot as plt

a = np.arange(256).reshape(16, 16)
w = 15
b = np.zeros([w] * 2)
for i in range(1, w // 2):
    b[i:-i, i:-i] = np.ones([w - 2 * i] * 2) if i % 2 else np.zeros([w - 2 * i] * 2)

#
plt.subplot(1, 2, 1).imshow(a, cmap="gray")
plt.subplot(1, 2, 2).imshow(b, cmap="gray")
plt.show()
