import numpy as np
import h5py

# create random array
data1 = np.random.random(size=(10000,200))

# save array
np.save('data1.npy', data1)
h5py.File('data1.h5','w').create_dataset("name-of-dataset", data = data1)

# read files
np_data_read = np.load('data1.npy')
h5_data_read = h5py.File('data1.h5','r')['name-of-dataset'][:]
