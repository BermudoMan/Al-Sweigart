# обход дерева каталогов с целью отбора файлов с заданным расширением

import os, shutil
#Z:\!GIT\Al-Sweigart\chapter9\task\23
def copy_pdf_to(folder):
#обход всех каталогов и подкаталогов

    for folder_name, subfolders, filenames in os.walk('.\\chapter9\\task\\'):
        print('Текущая папка - ' + folder_name)

        for subfolder in subfolders:
            print('Подпапка папки!' + folder_name + ': ' + subfolder)
            shutil.copy(subfolder, '.\\chapter9\\pdf_copies\\')

        for filename in filenames:
            print('Файл в папке ' + folder_name + ': ' + filename)
#            shutil.copy(filename, '.\\chapter9\\pdf_copies\\')




copy_pdf_to('.\\chapter9\\')
