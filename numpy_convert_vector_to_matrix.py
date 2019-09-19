import numpy as np

a = np.random.rand(20,10) # Matrix
b = np.random.rand(20)    # Vector
c = np.random.rand(20)    # Vector

b2 = np.expand_dims(b, axis=1) # converts to Matrix
c2 = np.expand_dims(c, axis=1) # converts to Matrix

x1 = np.hstack((a,b2,c2))

x2 = np.concatenate((a, b2, c2), axis=1)

# NOTE if using (a, b, c) => WON'T WORK!!! Mismatch!!
