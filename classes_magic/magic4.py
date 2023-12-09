class Person:
    def __init__(self, name, age)
        self.name = name
        self.age = age
    def __str__(self): # приментяется если вызывать не как функцию
        return f'Name: {self.name}. age: {self.age}'               
    def __call__(self, some_arg): # вызов объекта как функции
        return f'Я {self.name}! Кто меня вызвал {some_arg}?'

tom = Person('Tom', 23)
print(tom)
print(tom(2321))


