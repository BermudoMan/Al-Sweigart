class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name: {self.name}. age: {self.age}'        
    def __add__(self, another_person):
        return Person(self.name + another_person.name, self.age + another_person.age)
    def __eq__(self, another_person):
        return self.name == another_person.name
    def __pow__(self,indicator):
        return Person(f'{self.name}^{indicator}', self.age**indicator) # Person указывается, чтобы к выводу данной функции, применялась функция __str__ класса 
# вывод без Person(...) => ('Moxim^2', 529)
# вывод c Person(...) => Name: Moxim^2. age: 529

moxim = Person('Moxim', 23)
egor = Person('Егор', 24)
print(moxim + egor)

moxim_clone1 = Person('Moxim', 32)
moxim_clone2 = Person('Maxim', 32)
moxim_clone3 = Person('Moxim', 23)

print(moxim == moxim_clone1)
print(moxim == moxim_clone2)
print(moxim == moxim_clone3)
print(moxim ** 2)