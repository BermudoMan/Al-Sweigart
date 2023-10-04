#! python3
# pw.py - Программа для незащищенного хранения паролей.

PASSWORDS = {'email': 'F7min1BDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print("""Использование: python pw.py [имя учетной записи] -
          копирование пароля учетной записи""")
    sys.exit()

account = sys.argv[1] # первый аргумент командной строки - это
                      # имя учетной строки

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + ' скопирован в буфер.')
else:
    print('Учетная запись ' + account + 'отсутствует в списке.')
    