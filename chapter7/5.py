import re

hero_Regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_Regex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = hero_Regex.search('Tina Fey and Batman')
print(mo2.group())

print('-----------------1')

bat_Regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_Regex.search('Batmobile потерял колесо')
print(mo.group())
print(mo.group(1))

print('-----------------2')

bat_Regex = re.compile(r'Bat(wo)?man')
mo1 = bat_Regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_Regex.search('The Adventures of Batwoman')
print(mo2.group())

print('?-----------------3')

phone_num_Regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_num_Regex.search('Мой номер: 231-455-3211.')
print(mo1.group())
mo2 = phone_num_Regex.search('Мой номер: 455-3211.')
print(mo2.group())

print('*-----------------4')

bat_Regex = re.compile(r'Bat(wo)*man')
mo1 = bat_Regex.search('The Adventures of Batman')
mo2 = bat_Regex.search('The Adventures of Batwoman')
mo3 = bat_Regex.search('The Adventures of Batwowowowowoman')

print(mo1.group())
print(mo2.group())
print(mo3.group())

print('+-----------------5')

bat_Regex = re.compile(r'Bat(wo)+man')
mo1 = bat_Regex.search('The Adventures of Batwoman')
mo2 = bat_Regex.search('The Adventures of Batwowowowowoman')
try:
    mo3 = bat_Regex.search('The Adventures of Batman')
    if mo3 != None:
        print(mo3)
except:
    print(type(mo3))
    
print(mo1.group())
print(mo2.group())
