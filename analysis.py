from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.cos(x)

plots_dir = Path().cwd() / "plots"
plots_dir.mkdir(exist_ok=True)

# Madicken's favorite :P
with plt.rc_context({"image.cmap": "jet"}):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    fig.savefig(plots_dir / "cosine.png")
