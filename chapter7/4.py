#группы в регулярных выражениях
import re

phone_num_Regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_Regex.search('Мой номер: 231-455-3211.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())

print('---------------------------')
area_code, main_number = mo.groups()
print(area_code)
print(main_number)



print('---------------------------')
print('---------------------------')
phone_num_Regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phone_num_Regex.search('Мой номер: (231) 455-3211.')
print(mo.group(1))
print(mo.group(2))
