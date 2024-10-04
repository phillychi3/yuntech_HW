import numpy as np
import matplotlib.pyplot as plt

w = 16
a = np.zeros([w] * 2)
for i in range(1, w // 2):
    a[i:-i, i:-i] = (np.ones if i % 2 else np.zeros)([w - 2 * i] * 2)
    b = np.concatenate((a, a), axis=1)
    b = np.concatenate(
        (
            b,
            b,
        ),
        axis=0,
    )
    c = np.concatenate([np.concatenate([a] * 2)] * 3, axis=1)
    d = np.hstack([np.vstack([a] * 3)] * 2)


# plt.subplot(1, 2, 2).imshow(a, cmap='gray')

for i, _ in enumerate([a, b, c, d]):
    plt.subplot(2, 2, i + 1).imshow(_, cmap="gray")
plt.show()
