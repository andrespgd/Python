# append object at the end.

x = [1, 2, 3]
x.append([4, 5])
print (x)
# [1, 2, 3, [4, 5]]


# extend list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
# [1, 2, 3, 4, 5]


# add 2 lists

x = [1, 2, 3]
y = [4, 5]
z = x + y
print(z)
# [1, 2, 3, 4, 5]


# flatten list
```
values = [[1,2,3],[4,5,6],[7,8,9]]
import itertools
values_flatten = itertools.chain.from_iterable(values)
```


# permutations
```
import itertools
c = itertools.product((1,2,3), repeat=3)
list(c)
