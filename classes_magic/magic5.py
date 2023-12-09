class Person:
    def __init__(self, name, age)
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name: {self.name}. age: {self.age}' 
    def __enter__(self):
        print('=====START=====')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('=====END=====')

x = 0
with Person('Tom', 23) as tom:
    while x < 100: 
        x += 5
        print(f'some {x}')