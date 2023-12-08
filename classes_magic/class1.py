class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def say_hello(self, massage):
        print(f"Hello!{massage}")



#person1 = Person('Piter', 22)
#print(type(person1))
#print(type(Person))
#print(person1)

#person1.say_hello(', dude')