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


mcb_shelf.close()