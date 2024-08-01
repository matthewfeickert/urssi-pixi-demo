from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.cos(x)

plots_dir = Path().cwd() / "plots"
plots_dir.mkdir(exist_ok=True)

# Madicken's favorite :P
with plt.rc_context(rc={"image.cmap": "jet"}):
    fig, ax = plt.subplots()

    _cmap = plt.get_cmap()
    ax.set_prop_cycle("color", [_cmap(idx) for idx in np.linspace(0, 1, 10)])

    ax.plot(x, y, label=r"$\cos(x)$")
    ax.plot(x + 1, 2 * y, label=r"$2\cos(x+1)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.legend(frameon=False)

    fig.savefig(plots_dir / "cosine.png")
