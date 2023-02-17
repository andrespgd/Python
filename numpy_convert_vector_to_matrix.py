import numpy as np

a = np.random.rand(20,10) # Matrix (20,10)
b = np.random.rand(20)    # Vector (20,)
c = np.random.rand(20)    # Vector (20,)

b2 = np.expand_dims(b, axis=1) # Vector --> Matrix (20, 1)
c2 = np.expand_dims(c, axis=1) # Vector --> Matrix (20, 1)

x1 = np.hstack((a,b2,c2)) # Matrix (20, 12) # Matrix (20,12)

x2 = np.concatenate((a, b2, c2), axis=1) # Matrix (20, 12)

# NOTE if using (a, b, c) => WON'T WORK!!! Mismatch!!
