import matplotlib.pyplot as plt
import numpy as np



x = np.arange(0, 2 * np.pi, np.pi/100)
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)

fig,ax = plt.subplots()
ax = fig.add_subplot(221)
ax.plot(x,y)
ax = fig.add_subplot(222)
ax.plot(x,z)
ax = fig.add_subplot(212)
ax.plot(x,w)


fig,ax = plt.subplots()
ax = fig.add_subplot(211)
ax.plot(x,w)
ax = fig.add_subplot(223)
ax.plot(x,z)
ax = fig.add_subplot(224)
ax.plot(x,y)

plt.show()
