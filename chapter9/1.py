import shutil, os

shutil.copy('.\\1_from\\start.txt', \
            '.\\1_to')

shutil.copy('.\\1_from\\start.txt', \
            '.\\1_to\\start_with_new_name')

print('==============')
try:
    shutil.copytree('.\\1_from', '.\\!1_from_backup')
except:
    print('EXIST!')
print('==============')
# moving file start_new_name to 1_from folder

shutil.move('.\\1_to\\start_with_new_name', \
            '.\\1_from\\start_with_new_name_moved.txt')


