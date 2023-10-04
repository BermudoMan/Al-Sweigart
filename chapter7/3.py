import re

phone_num_Regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_Regex.search('Мой номер: 231-455-3211.')
#print(type(phone_num_Regex.search('Мой номер: 231-455-3211.')))
print(mo)
print('Найденный номер телефона: ' + mo.group())


#print(type(phone_num_Regex))
