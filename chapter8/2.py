import os

hello_file = open('Z:\\!GIT\\Al-SWEIGART\\chapter8\\2\\hello.txt')
hello_content = hello_file.read()
hello_content   
print('--------------------------------')

sonnetFile = open('Z:\\!GIT\\Al-SWEIGART\\chapter8\\2\\sonnet29.txt')
print(sonnetFile.readlines())

print('--------------------------------')
bacon = open('bacon.txt', 'w')
bacon.write('Hello world\n')
bacon.close
bacon = open('bacon.txt', 'r')
print(bacon.read())

bacon = open('bacon.txt', 'a')
bacon.write('Bacon is not a vegetable')
bacon.close()
bacon = open('bacon.txt', 'r')
print(bacon.read())
