'''
This code illustrates the need for __init__
'''



class Dog:
    kind = 'canine'  # shared amongst ALL 'dogs' that will be created
    tricks = []      # shared amongst ALL 'dogs' that will be created
    print('hi')
    def __init__(self,name,age):
        self.name = name
        self.age = age   
    def getName(self):
        return self.name      
    def getAge(self):
        return self.age     
    def addTrick(self,trick):
        self.tricks.append(trick)
           
yuyo = Dog('yuyo', 10)
yuyo.addTrick('runs_fast')
yuyo.addTrick('rolls')

print(yuyo.getName())
print(yuyo.getAge())
print(yuyo.tricks)
print()

matias = Dog('matias',20)
print(yuyo.getName())
print(yuyo.getAge())
print(matias.tricks) # Matias has the same trics added to Yuyo
print()





class Car:
    size  = 'large'
    wb    = 3.0
    mass  = 1000.0
    doors = 4
    use = ''
    color = ''
    
celica = Car
celica.size = 'small'
celica.wb = 1.9
celica.use = 'racing'

print(celica.size)
print(celica.wb)
print(celica.mass)
print(celica.doors)
print(celica.use)
print()

camry = Car
print(camry.wb) # no longer 3.0
