import os
print(os.path.join('usr', 'bin', 'spam'))

print('--------------------------------')

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join('C:\\Users\\Ivan', filename))

print('--------------------------------')

#текущий рабочий каталог
print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())
os.chdir('Z:\\!GIT\\Al-SWEIGART')
print(os.getcwd())

#os.makedirs('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1')
print('--------------------------------')

print(os.path.abspath('.'))
print(os.path.abspath('.\\1'))

print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.\\1')))

print('--------------------------------')

print(os.path.dirname('Z:\\!GIT\\Al-SWEIGART'))
print(os.path.basename('Z:\\!GIT\\Al-SWEIGART'))
#как строка
print(os.path.split('Z:\\!GIT\\Al-SWEIGART'))
#как список
x = 'Z:\\!GIT\\Al-SWEIGART'
print(x.split(os.path.sep))

print('--------------------------------')

print(os.path.getsize('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1\\pic.jpg'))
print(os.listdir('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1'))

#суммарный размер файлов

total_size = 0
for filename in os.listdir('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1'):
    total_size = total_size + os.path.getsize(os.path.join('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1', filename))
print(total_size)

print('--------------------------------')

#проверка существования пути

print(os.path.exists('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1'))
print(os.path.exists('D:\\!GIT\\Al-SWEIGART\\chapter8\\1'))
print(os.path.isfile('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1'))
print(os.path.isdir('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1'))
print(os.path.isfile('Z:\\!GIT\\Al-SWEIGART\\chapter8\\1\\pic.jpg'))

#проверка наличия флешки

print(os.path.exists('D:\\'))

print('--------------------------------')
