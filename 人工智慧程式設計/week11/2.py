import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def clean(ax):
    ax.axis('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[:].set_visible(False)
    return ax


x, y, z = 4, 400, 0
a, b = 0, 1
delta, theta = np.pi / 20, np.linspace(0, 2 * np.pi * x, y)
r = a + b * theta
fg, ax = plt.subplots()
ln, = clean(ax).plot([], [], 'g', lw=15)
_ = (x + 2) * 2 * np.pi
ax.set_xlim(-_, _)
ax.set_ylim(-_, _)


def bsw():
    return ln,


def xsw(i):
    global theta
    theta += delta
    ln.set_data(r * np.cos(theta), r * np.sin(theta))
    return ln,


_ = FuncAnimation(fg, xsw, 120, bsw, blit=True, interval=50)
plt.show()