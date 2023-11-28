#plots a bar graph


import numpy as np
import matplotlib.pyplot as plt

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 2, 45]

plt.bar(x, y, color="r", align="edge", width=0.5, edgecolor="green", lw=6)
plt.show()