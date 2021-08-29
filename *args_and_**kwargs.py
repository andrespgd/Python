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





