import numpy as np
import matplotlib.pyplot as plt
 
# WORKS
image1 = np.random.rand(100,32,32,3)
print('image shape=', image1.shape)
plt.imshow(image1[1])
plt.show()

# WORKS
image1 = np.random.rand(100,32,32)
print('image shape=', image1.shape)
plt.imshow(image1[1])
plt.show()

# THIS WILL NOT WORK, TO FIX IT REMOVE THE EXTRA UNUSED DIMENSION by SQUEEZE
image1 = np.random.rand(100,32,32,1)
image1 = image1.squeeze()
print('image shape=', image1.shape)
plt.imshow(image1[1])
plt.show()

# THIS WILL NOT WORK => ERROR
image1 = np.random.rand(100,32,32,1)
print('image shape=', image1.shape)
plt.imshow(image1[1])
plt.show()
