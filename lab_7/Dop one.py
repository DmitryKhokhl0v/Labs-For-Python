import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter


def update(i):
    dot.set_data(i, np.sin(i))
    return dot,


fig, ax = plt.subplots()
x = np.arange(0, 5 * np.pi, 0.001)
y = np.sin(x)
line = plt.plot(x, y)
ax.set_title('y = sin(x)')
ax = plt.axis([0, 5 * np.pi, -1.2, 1.2])
dot, = plt.plot(0, np.sin(0), 'kx')

animation = FuncAnimation(fig, update, frames=np.arange(0, 5 * np.pi, 0.1), interval=30, repeat=True)
plt.show()
animation.save('sin(x).gif', writer=PillowWriter(fps=30))
