j = 'Hello world!'

print(j.endswith('!'))
print(j.endswith('world!'))
print(j.endswith('world'))

print(j.startswith('H'))
print(j.startswith('e'))
print(j.startswith('Hello'))

print(j.startswith('Hello world!'))
print(j.endswith('Hello world!'))

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print('ABC'.join(['cats', 'rats', 'bats']))

print('cats, rats, bats'.split(' ,'))
print('cats, rats, bats'.split(','))
print('cats, rats, bats'.split('a'))

#выравнивание текста

print('hello'.rjust(10))
print('hello'.rjust(40, '_'))
print('hello'.ljust(120, '*'))
print('hello'.center(10))
print('hello'.center(100, '_'))
print('hello'.center(120, '='))
