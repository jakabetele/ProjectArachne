import numpy as np
import random
import matplotlib.pyplot as plt


mean = 0
std = 1

nr_all = []

for i in range(100000):
    v = random.gauss(mean, std)
    nr_all.append(v)

plt.hist(nr_all, 12)
plt.show()
