import multiprocessing
import numpy as np
import time
import cupy as cp

# Code to compare inverting a large matrix

n_iters = 10
m_size = 2000

title = '1- Using Numpy'
s = time.time()
for i in range(n_iters):
    A = np.random.rand(m_size,m_size)
    B = np.linalg.inv(A)
    print('iter',i)
e = time.time()
print(title, e-s,'secs')

title = '2- Using Cupy'
s = time.time()
for i in range(n_iters):
    A = cp.random.rand(m_size,m_size)
    B = cp.linalg.inv(A)
    print('iter',i)
    cp.cuda.Stream.null.synchronize()
e = time.time()
print(title, e-s,'secs')

title = '3- Using Multiprocessing'
s = time.time()
def f(x):
    return np.linalg.inv(x)
num_proc = multiprocessing.cpu_count()
for i in range(n_iters):
    A = np.random.rand(m_size,m_size)
    p = multiprocessing.Pool(num_proc - 1)
    B = p.map(f, [A, A])
    print('iter',i)    
e = time.time()
print(title, e-s,'secs')

