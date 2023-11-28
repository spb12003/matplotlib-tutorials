#plot multiple lines, legend


import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

a = [100, 102, 99, 101, 100, 102]
b = [99, 105, 112, 125, 140, 144]
c = [100, 99, 95, 91, 89, 75]

plt.plot(a, label="Company1")
plt.plot(b, label="Company2")
plt.plot(c, label="Company3")

plt.legend(loc="lower center")

plt.show()