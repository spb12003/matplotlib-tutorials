#plots a pie chart


import numpy as np
import matplotlib.pyplot as plt

lang = ["C++", "C#", "Python", "Java", "Go"]
votes = [20, 50, 140, 25, 45]
explodes = [0.3, 0, 0, 0, 0]   ##Separates sections of the pie chart

plt.pie(votes, labels=lang, explode=explodes, autopct="%.2f%%", pctdistance=1.3, startangle=90)
plt.show()