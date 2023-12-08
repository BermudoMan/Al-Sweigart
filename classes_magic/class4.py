from class1 import Person

tom = Person('Tom', 34)
print(tom)
print(tom.name)
print(tom.age)
tom.age = 36
print(tom)
print(tom.name)
print(tom.age)

# создание доп. атрибута
tom.company = "Disney"
print(tom.company)