import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

fig, ax = plt.subplots(layout="constrained")

ax.plot(
    x,
    np.sin(4 * np.pi * x),
    color='red',
    marker='.',
    linestyle='none',
)

ax.set(
    xlabel=r"$t / \mathrm{s}$",
    ylabel=r"$U / \mathrm{V}$",
    title="Sine",
)

fig.savefig("build/plot.pdf")
