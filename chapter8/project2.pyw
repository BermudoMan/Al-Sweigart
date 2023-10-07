#! python3
# project2.pyw - сохраняет и загружает фрагменты текста в буфер обмена
# Использование: py.exe project2.pyw save <ключевое слово> -
#                   сохраняет буфер обмена в ключевое слово
#                py.exe project2.pyw <ключевое слово> - 
#                   загружает ключевое слово в буфер обмена
#                py.exe project2.pyw list -
#                   загружает все ключевые слова в буфер обмена

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# сохранение содержимого в буфер обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # формирование списка ключевых слов и загрузить содержимое
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argb[1]])
mcb_shelf.close()