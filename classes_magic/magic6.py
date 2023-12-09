class Persons:
    def __init__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    

#persons = Persons(['Tom', 'Angela', 'Igor', 'Samuel', 'Kassandra'])
name_list = Persons()
myiter = iter(name_list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
