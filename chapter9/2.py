#обход всех каталогов и подкаталогов

import os 

for folder_name, subfolders, filenames in os.walk('.\\chapter9\\2'):
    print('Текущая папка - ' + folder_name)

    for subfolder in subfolders:
        print('Подпапка папки!' + folder_name + ': ' + subfolder)
    
    for filename in filenames:
        print('Файл в папке ' + folder_name + ': ' + filename)