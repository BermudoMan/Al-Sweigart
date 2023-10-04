cats_names = []
while True:
    print('Enter the name of cat ' + str(len(cats_names) + 1) +  '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cats_names = cats_names + [name]
print('The cat name are:')
for name in cats_names:
    print(' ' + name)