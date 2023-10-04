#! python3
#GLOBAL! поиск всех мобильных номеров и адресов эл. почты

import re, pyperclip

#1)рег. выражение для номера телефона
phone_Regex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?              #территориальный код
            (\s|-|\.)?                      #разделитель
            (\d{3})                         #первые 3 цифры
            (\s|-|\.)                       #разделитель
            (\d{4})                         #последние 4 цифры
            (\s*(ext|x|extt.)\s*(\d{2,5}))? #добавочный номер    
)''', re.VERBOSE)

#2)рег. выражение для email
email_Regex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+       #имя пользователя
            @                       #собака
            [a-zA-Z0-9.-]+          #имя домена
            (\.[a-zA-Z]{2-4})       #остальная часть адреса                         
)''', re.VERBOSE)

#3)поиск совпадений в тексте буфера обмена
text = str(pyperclip.paste())
matches = []
for groups in phone_Regex.findall(text):
    phone_Num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_Num += ' x' + groups[8]
    matches.append(phone_Num)
for groups in email_Regex.findall(text):
    matches.append(groups[0])

#4)объединение совпадений в одну строку для копир. в буфер
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Тел. номера и emails не обнаружены!')
