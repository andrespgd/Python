def add(a, b,c):
    print(a+b+c)
     
add(2,3,4)
print() 
 

### args ###

def add(*args):
    total = 0
    for arg in args:
        total+=arg
    print(total)
    
add(2,3,4)
add(2,3,4,6,7,9)
print()



def func(*args):
    for arg in args:
        print(arg)
 
l = [11,3,4,5,"tuts"]
func(l)
print('This prints the list as a whole, because its interpreting the list as one item.')
print()
func(*l)
print('The * will unpack the list and output each individual list item.')
print()



### Kwargs ###
'''
Kwargs uses value pairs, notation is double asterisk (**)
'''

def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
myFun(first ='Geeks', mid ='for', last='Geeks') 
print()



### arg and Kwargs ###

def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print(arg1)
        print ("%s == %s" %(key, value))
 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks') 
print()



### *args and **kwargs ###

def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)

myFun('geeks',' for', 'geeks', first="Geeks", mid="for", last="Geeks")




#################################  EDIT

class Foo1:
    def __init__(self, **kwargs):
        self.a = kwargs['a']
        self.b = kwargs['b']

foo1 = Foo1(a=1, b=2)
print(foo1.a)  # 1
print(foo1.b)  # 2
print(foo1.__dict__)  # {'a': 1, 'b': 2}


class MathematicalModel:
    def __init__(self, var1, var2, var3, **kwargs):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.__dict__.update(kwargs)  # Store all the extra variables

#################################  EDIT

def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)
	
	
connect() 
# <class 'dict'>
# {}

connect(server='localhost', port=3306, user='root', password='Py1hon!Xt')
# <class 'dict'>
# {'server': 'localhost', 'port': 3306, 'user': 'root', 'password': 'Py1hon!Xt'}

# If you want to pass a dictionary to the function, you need to add two stars (**) to the argument like this:

def connect(**kwargs):
    print(kwargs)

config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

connect(**config)


