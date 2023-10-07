import os

print(os.getcwd())

start = open('.\\task2\\start.txt', 'r')
finish = open('.\\task2\\finish.txt', 'w')

print('Введите прилагательное')
adj = input()
print('Введите существительное')
noun1 = input()
print('Введите глагол')
verb = input()
print('Введите существительное')
noun2 = input()

x = str(start.readlines()).split(' ')
z = 0

for i in x:
    if i == 'ADJECTIVE':
        finish.write(adj + ' ')
    elif i == 'NOUN' and z == 0:
        finish.write(noun1 + ' ')
        z = z + 1
    elif i == 'VERB.':
        finish.write(verb + ' ')
    elif i == 'NOUN' and z != 0:
        finish.write(noun2 + ' ')
    else:
        finish.write(i + ' ')

start.close()
finish.close()
