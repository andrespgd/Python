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
