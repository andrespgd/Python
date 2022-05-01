# Annotations just tell the user what to expect for inputs and output types

# NOTE: it does NOT set the input nor output type (it has NO effect on the input or return type!!!)

def add_int(a:int, b:int) -> float:
    return a+b
  
x=add_int(1,1)
print(x)
print(type(x))
print(add_int.__annotations__)
'''
2
<class 'int'>
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'float'>}
'''


print()

x=add_int(10.5,10.5)
print(x)
print(type(x))
print(add_int.__annotations__)
'''
21.0
<class 'float'>
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'float'>}
'''
