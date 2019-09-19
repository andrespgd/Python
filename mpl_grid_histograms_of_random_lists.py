import matplotlib.pyplot as plt
import numpy as np
import random

# 1 - Create a list of matrix random size, with random NP vectors
data = []
for i in range(random.randint(0,10)):
    datai = []
    for j in range(random.randint(0,10)):
        x = np.random.random(100)
        datai.append(x)
    data.append(datai)


lsize =[]
for data0 in data:
    lsize.append(len(data0))
max_lsize = max(lsize)    

title = 'histogram plots in grid'
fig, ax = plt.subplots(len(data), max_lsize, sharex=True, sharey=True)
for i in range(len(data)):
    for j in range(len(data[i])):
        ax[i,j].hist(data[i][j], np.arange(0.0, 1.0, 0.1))
fig.suptitle(title, fontsize=20)
plt.show()
