#! python3
# maplt.py - запускает карту в браузере, извлекая почтовый адрес из командной строки
#            или буфера обмена

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # получение почтового адреса из командной строки
    address = ' '.join(sys.argv[1:])
else:
    # получение адресв из буфера обмена
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
