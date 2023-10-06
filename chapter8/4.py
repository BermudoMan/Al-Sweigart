#сохранение переменных в .py
import pprint

cats = [{'name': 'Jordie', 'desc': 'mad'}, 
        {'name': 'Basya', 'desc': 'chubby'}]

pprint.pprint(cats)
print(pprint.pformat(cats))
print(type(pprint.pprint(cats)))
print(type(pprint.pformat(cats)))

file_obj = open('.\\chapter8\\4\\my_cats.py', 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')
file_obj.close()


