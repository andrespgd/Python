import numpy as np

#simple NP array
x = np.random.random((10,2))

#list of 2 NP array os same dimension
y = [np.random.random((10,2)), np.random.random((10,2))]

#list of 2 NP array of different dimension
z = [np.random.random((10,2)), np.random.random((10,5))]


np.save('x.npy', x)

xx = np.load('x.npy')


np.save('y.npy', y)

yy = np.load('y.npy')


np.save('z.npy', z)

zz = np.load('z.npy', allow_pickle=True) #otherwise error loading
