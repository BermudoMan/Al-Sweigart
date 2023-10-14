#! python3
# backupToZip.py - копирует папку вместе со всем ее содержимым 
# в zip-файл с инкрементируемым номером копии в имени файла

import zipfile, os

def backup_to_zip(folder):
    # создание резервной копии всего содержимого папки "folder"

    folder = os.path.abspath(folder) # убедиться что задан абс. путь

    # определить, какое имя файла должен использовать код
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + \
                        str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1
    
    # создание zip

    print('Создается файл %s...' % (zip_file_name))
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')

    # обход всего дерева папки и сжатие файлов, содержащихся в каждой папке
    for foldername, subfolders, filenames in os.walk(folder):
        print('Добавление файлов из папки %s...' % (foldername))
        # добавить в zip-файл текущую папку
        backup_zip.write(foldername)
        # добавить в zip-файл все файлы из данной папки
        for filename in filenames:
            new_base / os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip')
                continue # не создавать резервные копии zip файлов
            backup_zip.write(os.path.join(foldername, filename))
        backup_zip.close()
        print('Готово')
