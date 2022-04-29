print('---------- args -------------')

def add(*args):
    total = 0
    for arg in args:
        total+=arg
    print('the sum of', *args, 'is =', total)
    
add(2,3,4)
print()


def func(*args):
    for arg in args:
        print(arg)
 
l = [11,3,4,5,'tuts']
print('This prints the list as one item:')
func(l)
print('* unpacks the list and outputs each individual item:')
func(*l)
print()



print('---------- Kwargs -------------')
'''
-uses value pairs
-notation is **
'''

def myFun1(**kwargs):
    for key, value in kwargs.items():
        print ('%s == %s' %(key, value))
 
myFun1(first='Geeks', mid='for', last='Geeks') 
print()
myFun1(**{'first':'Geeks', 'mid':'for', 'last':'Geeks'})
print()


def myFun2(arg1, **kwargs):
    for key, value in kwargs.items():
        print(arg1)
        print ('%s == %s' %(key, value))
 
myFun2('Hello', first='Geeks', mid='for', last='Geeks') 
print()


def myFun3(*args,**kwargs):
	print('args: ',   type(args),   args)
	print('kwargs: ', type(kwargs), kwargs)

myFun3('geeks',' for', 'geeks', first='Geeks', mid='for', last='Geeks')
print()


print('---------- Function with Kwargs -------------')

def connect(**kwargs):
    print(type(kwargs), kwargs)
	
connect() 
print()

connect(server='localhost', port=3306, user='root', password='123')
print()


print('---------- Function with Kwargs - Pass a dictionary -------------')

config = {'server':'localhost', 'port':3306, 'user':'root', 'password':'123'}

connect(**config)
print()


print('---------- Class with Kwargs -------------')

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
