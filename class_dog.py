class Dog():
    # class variables
    kind = 'canine'
    extinction = False
    def __init__(self, name, age, breed=None):
        # attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.color = None
        self.tricks = []
        self.vaccines = []
    # methods
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    # behavior method
    def add_trick(self, trick):
        self.tricks.append(trick)
        
        
print('Create Yuyo')
yuyo = Dog('yuyo', 10)
print(vars(yuyo))
yuyo.get_name()          
yuyo.add_trick('runs_fast')
yuyo.add_trick('rolls')
print(yuyo.tricks)
print(vars(yuyo))
yuyo.vaccines.append('distemper')
print(vars(yuyo))
print()

print('Create Matias')
matias = Dog('matias', 5, 'Poodle')
print(vars(matias))
# create a new attribute for an instance
matias.playful = True
print(vars(matias))
print()

print('Change a class variable for an instance only')
matias.extinction = True
print(yuyo.extinction)
print(matias.extinction)
print()

print('Change a class variable for ALL members of the class')
Dog.kind = 'cat'
print(yuyo.kind)
print(matias.kind)

print()
print(vars(yuyo))

print()
print(vars(matias))
