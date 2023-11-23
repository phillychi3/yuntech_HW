import numpy as np
import matplotlib.pyplot as plt

圓拉 = 1
點拉 = 400
圖編號 = 0
旋轉角度 = np.radians(90)
for 分母 in range(1,8):
    系塔 = np.linspace(0,2*np.pi*圓拉*分母,點拉*分母)
    for 粉子 in range(1,8):
        r = np.cos(粉子/分母*系塔)
        ax = plt.subplot(7,7,圖編號:=圖編號+1)
        ax.axis('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines[:].set_visible(False)
        ax.plot(r*np.cos(系塔 + 旋轉角度),r*np.sin(系塔 + 旋轉角度))

plt.show()

def test(): / print("lol")
