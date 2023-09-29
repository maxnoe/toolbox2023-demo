import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)

fig, ax = plt.subplots()

ax.plot(x, np.sin(2 * np.pi * x))

ax.set(
    xlabel="t / s",
    ylabel="U / V",
)

fig.savefig("plot.pdf")