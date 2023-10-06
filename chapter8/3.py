#сохранение переменных в двоичном формате .dat 
import shelve

shelf_file = shelve.open('.\\chapter8\\3\\mydata')
cats = ['Jordie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()

print('Check save correctness')

shelf_file = shelve.open('.\\chapter8\\3\\mydata')
print(type(shelf_file))
print(shelf_file['cats'])
shelf_file.close()

print('--------------------------------')

shelf_file = shelve.open('.\\chapter8\\3\\mydata')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()

print('--------------------------------')

