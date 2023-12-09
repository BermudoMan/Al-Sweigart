class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

tom = Person('Tom', 23)
print(tom)


class Person2:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name: {self.name}. age: {self.age}'
    
tom = Person2('Tom', 23)
print(tom)
#print(dir(tom)) # all possible fucnctions for 'tom' object
print(dir(object))
