# обход дерева каталогов с целью отбора файлов с заданным расширением

import os, shutil, re
#Z:\!GIT\Al-Sweigart\chapter9\task\23
def copy_pdf_to(folder):
    folder_from = 'Z:\\!GIT\\Al-Sweigart\\chapter9\\task\\'
    folder_to = 'Z:\\!GIT\\Al-Sweigart\\chapter9\\pdf_copy'
    reg = re.compile(r'\S*.pdf')
    
#обход всех каталогов и подкаталогов

    for folder_name, subfolders, filenames in os.walk(folder_from):
#        print('Текущая папка - ' + folder_name)
        for filename in filenames:
#            print(os.path.join(folder_name, filename))
            try:
                searched = reg.search(filename)
                way = searched.group()
#                shutil.copy(folder_from + way, folder_to)
                shutil.copy(folder_from + way, folder_to)                
            except:
                print('')

        for filename in subfolders:
            os.chdir(os.path.join(folder_from, filename))
            print(os.path.join(folder_from, filename))
            x = os.listdir(os.path.join(folder_from, filename))
            for i in x:
                y = os.path.join(folder_from, filename) + '\\' + i
                print(y)
                try:
                    searched = reg.search(y)
                    way = searched.group()
    #                shutil.copy(folder_from + way, folder_to)
                    shutil.copy(y, folder_to)                
                except:
                    print('')            
#            
#            print(searched.group())
 #           shutil.copy(searched.group(), folder_to)


copy_pdf_to('.\\chapter9\\')