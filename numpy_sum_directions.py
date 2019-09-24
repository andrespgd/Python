import numpy as np

x = np.array([
[1,2,3],
[4,5,6]])

#sum whole array
sum_x = x.sum()
print(sum_x)

#sum on this direction
# |
# |
# |
# V
sum_0dir = x.sum(axis=0)
print(sum_0dir)

#sum on this direction
# ------------>
sum_1dir = x.sum(axis=1)
print(sum_1dir)
