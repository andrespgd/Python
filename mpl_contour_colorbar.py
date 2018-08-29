import numpy as np
import matplotlib.pyplot as plt

xi = np.array([0., 0.5, 1.0])
yi = np.array([0., 0.5, 1.0])
zi = np.array([[0., 1.0, 2.0],
               [0., 1.0, 2.0],
               [-0.1, 1.0, 2.0]])

# colorbar
v = np.linspace(-.1, 2.0, 15, endpoint=True)

# plots color surface
plt.contour(xi, yi, zi, v, linewidths=0.5, colors='k')

# plots lines
plt.contourf(xi, yi, zi, v, cmap=plt.cm.jet)

# plots colorbar ticks
x = plt.colorbar(ticks=v)
print(x)

plt.show()
