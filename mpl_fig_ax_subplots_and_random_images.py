import numpy as np
import matplotlib.pyplot as plt


fig,ax = plt.subplots()
for i in range(43):    
    ax = fig.add_subplot(5,9,i+1)
    ax.set_title('image'+str(i))
    x_1channel = np.random.rand(43,32,32)
    ax.imshow(x_1channel[i])

fig,ax = plt.subplots()
for i in range(43):    
    ax = fig.add_subplot(5,9,i+1)
    ax.set_title('image'+str(i))
    x_3channel = np.random.rand(43,32,32,3)
    ax.imshow(x_3channel[i])

plt.show()
