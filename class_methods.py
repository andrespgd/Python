class MyClass:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(f"My name is {self.name}")

    @classmethod
    def class_method(cls):
        print(f"My class name is {cls.__name__}")

    @staticmethod
    def static_method():
        print("I am a static method")

my_instance = MyClass("Alice")
my_instance.instance_method()
MyClass.class_method()
MyClass.static_method()
