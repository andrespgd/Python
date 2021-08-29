'''
CLASS
-instance variable convention: use lowercase_with_underscore or initialLowerWithCaps
-class name convention: InitialCaps 
'''

# make sure to use (object) for new style of Python class
class House(object):
    # class variables, shared amongst ALL houses that will be created
    market = 'down' 
    def __init__(self, address, size, additions):
        # instance variables
        self.address = address
        self.size = size   
        self.additions = additions
    def add_additions(self, addition):
        self.additions.append(addition)
    
h1 = House('1st st', 1000.0, ['sunroom'])

h2 = House('2nd st', 2000,   ['sunroom', 'garage'])

h3 = House('3rd st', 3000.0, [])
h3.add_additions('second_room')


print()
print('--instance type--')
print(type(h1)) 

print()
print('--instance variables--')
print(dir(h1)) # all attributes
print(vars(h1).keys()) # instance variables keys
print(vars(h1)) # instance variables
# OR
print(h1.__dict__.keys())
print(h1.size) # specific instance variable

print()
print('--class variables--')
print(h1.market, h2.market, h3.market)
print(House.market)
House.market = 'up'
print(h1.market, h2.market, h3.market)
print(House.market)
h1.market = 'down'
print(h1.market, h2.market, h3.market)
print(House.market)






'''
EMPTY CLASS
Sometimes it is useful to have a data type similar C “struct”.
An empty class definition will do nicely.
'''

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
