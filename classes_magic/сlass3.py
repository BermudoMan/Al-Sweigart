# __init__ - конструктор 1)неявно существует всегда = отвечает за создание самого класса
# 2) в __init__ указываются переменные(основные) для каждого экземпляра, относящегося к классу Person
# 3) вне блока с __init__ можно указывать переменные общие для всех экземпляров класса
class Person:
    general_v = 'Я: '
    type = 'some_man'
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('Создание объекта класса Person')
    def say_name(self):
        print(self.general_v + f'My name is {self.name}.')
    def second_question(self):
        print(self.general_v + f'I am {self.age} old. Я дед')

class Interviewer:
    general_v = 'Интервьювер: '
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def say(self, question):
        self.question = question
        print(self.general_v + f'{question}?')
        

tom = Person('Tomas', 77)
di = Interviewer('Diana', 'product-manager')

# Dialog
di.say('What is your name')
tom.say_name()
di.say('How old are you')
tom.second_question()
print(Person.type)
