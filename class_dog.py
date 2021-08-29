'''
This code illustrates the need for __init__
'''


class Dog:
    kind = 'canine'  # class variable
    tricks = []      # class variable
    print('hi')
    def __init__(self,name,age):
        self.name = name # instance variable
        self.age = age   # instance variable
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

