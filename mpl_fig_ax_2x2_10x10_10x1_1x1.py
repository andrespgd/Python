import matplotlib.pyplot as plt
import numpy as np
import random

x = np.linspace(0, 10 * np.pi , 1000)
y = []
for i in range(100):
    s = np.sin(x + random.uniform(-1, 1) * np.pi) * random.uniform(0, 1)
    y.append(s)

signal_name = []
for i in range(100):
    name = 'signal_' + str(i)
    signal_name.append(name)
    
# 2x2 case    
fig, ax = plt.subplots(2, 2)
ax[0,0].plot(x, y[0])
ax[0,1].scatter(x, y[1])
ax[1,0].scatter(x, y[2])
ax[1,1].plot(x, y[3])
plt.show()

# 10x10 case
fig, ax = plt.subplots(10, 10, sharex=True, sharey=True)
for i in range(10):
    for j in range(10):
        ax[i,j].plot(x, y[10*j + i])
plt.show()

# 10x1 case
fig, ax = plt.subplots(10, 1, sharex=True)
fig.subplots_adjust(hspace=0)
for i in range(10):
    ax[i].plot(x, y[i])
    ax[i].set_title(signal_name[i], loc='right', pad=-10)
plt.show()

# 1x1 case
fig, ax = plt.subplots(1, 1)
ax.plot(x, y[0])
ax.plot(x, y[1])
ax.plot(x, y[2])
ax.plot(x, y[3])
plt.show()


# 1x1 case - square grid shape
fig, ax = plt.subplots(1, 1)
ax.plot(x, y[0])
ax.plot(x, y[1])
ax.plot(x, y[2])
ax.plot(x, y[3])
ax.set_aspect('equal','box')
plt.show()
