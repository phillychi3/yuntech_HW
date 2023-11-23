import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and subplots
fig, axes = plt.subplots(7, 7, figsize=(14, 14))
plt.subplots_adjust(wspace=0, hspace=0)

# Set up the initial parameters for the spirals
a, b, c = 1, 400, 0
delta = np.pi / 20

# Create a function to initialize the subplots


def init_subplots():
    for ax in axes.flat:
        ax.axis('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines[:].set_visible(False)


# Initialize the subplots
init_subplots()

# Create the animation function


def animate(i):
    global c
    c = 0
    for ax_row in axes:
        for ax in ax_row:
            ax.cla()
            ax.axis('equal')
            ax.set_xticks([])
            ax.set_yticks([])
            ax.spines[:].set_visible(False)

            theta = np.linspace(0, 2 * np.pi * a * (c // 7 + 1), b * (c // 7 + 1))
            r = np.cos((c % 7 + 1) / (c // 7 + 1) * (theta + delta * i))

            ax.plot(r * np.cos(theta), r * np.sin(theta))
            c += 1


# Create the FuncAnimation object
ani = FuncAnimation(fig, animate, frames=np.arange(0, 120), interval=1)

# Show the animation
plt.show()