#plots line graph


import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 82, 89, 80, 79, 91, 88, 87, 81, 80, 89, 88]

plt.plot(years, weights, c="r", lw=2, linestyle="--")
plt.show()