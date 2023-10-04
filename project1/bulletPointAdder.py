#! python 3
# bulletPointAdder.py - Добавляет маркеры Википедии в начало
# каждой строки текста, сохраненного в буфере обмена

import pyperclip
text = pyperclip.paste()

# Разделить и добавить звездочки.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] + '* ' + lines[i]   

text = '\n'.join(lines)
pyperclip.copy(text)
