# переименование файлов с заменой американского формата дат европейскими

#! python3
# rename_dates.py - Переименовывает файлы, имена которых включают 
# даты, указанные в амер. формате (ММ-ДД-ГГГГ) в евро формат (ДД-ММ-ГГГГ)

import os, re, shutil

# рег. выражение
date = re.compile(r"""^(.*?)
                  ((0|1)?\d)-
                  ((0|1|2|3)?\d)-
                  ((19|20)\d\d)
                  (.*?)$
                  """, re.VERBOSE)

# орг-я цикла по файлам в рабочем каталоге
for amer_filename in os.listdir('.'):
    mo = date.search(amer_filename)
    # пропуск файлов с именами, не содержащими дат
    if mo == None:
        continue

    # получение отдельных частей имен файлов
    before_part = mo.group(1)
    mounth_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # формирование имен, соответствующих европейскому стилю
    euro_filename = before_part + day_part +'-' + mounth_part + \
        + '-' + year_part + after_part
    
    # получение полных абсолютных путей к файлам
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # переименование файлов
    print('Заменяем имя "%s" именем "%s" ...' \
          % (amer_filename, euro_filename))
    
