#Plots a scatter plot of random x, y data:


import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1000) * 100   ## random values within 0 - 100
y_data = np.random.random(1000) * 100

plt.scatter(x_data, y_data, c="#00f", s=25, marker="*", alpha=0.3)
plt.show()