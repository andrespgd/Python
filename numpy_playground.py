import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a.shape)
print(a.dtype, '\n')

a[:,2] = (a[:,2] - 100)/100
print(a)
print(a.shape)
print(a.dtype, '\n')

b = np.random.random((2, 3, 4))
print(b)
print(b.shape)
print(b.dtype, '\n')


b[:,:,0] = (b[:,:,0] - 100.0) / 100.0
print(b)
print(b.shape)
print(b.dtype, '\n')


# convert vector to column array
feature_list = [0.5,0.3,0.0,5.0,2.0]
X = np.vstack(feature_list).astype(np.float64)

