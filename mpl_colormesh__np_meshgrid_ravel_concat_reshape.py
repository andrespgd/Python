import numpy as np
import matplotlib.pyplot as plt

xx, yy = np.meshgrid(np.arange(0, 10, 1), np.arange(0, 100, 10))
print('xx \n', xx, '\n')
print('yy \n', yy, '\n')

xx_ravel = xx.ravel()
yy_ravel = yy.ravel()
print('xx_ravel \n', xx_ravel, '\n')
print('yy_ravel \n', yy_ravel, '\n')

xxyy_ravel_concatenated = np.c_[xx_ravel, yy_ravel]
print('xxyy_ravel_concatenated \n', xxyy_ravel_concatenated, '\n')

# add function
def xplusy(a):
    return a[:,0] + a[:,1]

Z = xplusy(xxyy_ravel_concatenated)
print('Z = xplusy', '\n', Z, '\n')

Z = Z.reshape(xx.shape)
print('Z.reshape', '\n', Z, '\n')

# meshplot of xx yy Z
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.jet, edgecolors='k')
