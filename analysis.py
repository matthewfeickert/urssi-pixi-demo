import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.savefig("cosine.png")
