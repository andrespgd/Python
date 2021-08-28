class MyClass:
    x = 3
    print('Created!')

a = MyClass() # Will output 'Created!'
a = MyClass() # Will output nothing since the class already exists!
a = MyClass() # Will output nothing since the class already exists!
a = MyClass() # Will output nothing since the class already exists!

''' 
 In this example, without __init__ initializes an attribute 
 that is shared among all instances of a class.
 '''



class MyClass:
    def __init__ (self):
        self.x = 3
        print('Created!')

a = MyClass() # Will output 'Created!'
a = MyClass() # Will output 'Created!'
a = MyClass() # Will output 'Created!'
a = MyClass() # Will output 'Created!'

'''
__init__ is used to initialize the state of multiple instances of a class
 where each instance's state is decoupled from each other.
'''
