class Dog:
    
    kind = 'canine'
    
    tricks = []
    
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

print(yuyo.getName())
print(yuyo.getAge())

yuyo.addTrick('runs_fast')
yuyo.addTrick('rolls')

print(yuyo.tricks)


print('/n VERY SIMPLE CLASS')
class Car:
    size  = 'large'
    wb    = 3.0
    mass  = 1000.0
    doors = 4
    use = ''
    color = ''
    
celica = Car
celica.size = 'small'
wb = 1.9
mass = 800
doors = 2
celica.use = 'racing'
