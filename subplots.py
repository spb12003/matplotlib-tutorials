#subplots... why isn't it working?


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Wave")

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine Wave")

fig.suptitle("Four Plots")
plt.show()