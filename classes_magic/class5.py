class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def info(self):
        print(f"Name: {self.name}  Age: {self.age}")

tom = Person('Tom')
tom.age = 37
tom.info()