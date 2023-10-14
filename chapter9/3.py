#архивирование
import zipfile, os

os.chdir('.\\chapter9\\')
exampleZip = zipfile.ZipFile('3.zip')
print(exampleZip.namelist())

some_textInfo = exampleZip.getinfo('3/2_1/2_1_1/some_text.txt')

print(some_textInfo.file_size)
print(some_textInfo.compress_size)

print('Сжатый файл в %s раза меньше!' % (round(some_textInfo.file_size \
                                        / some_textInfo.compress_size, 2)))
exampleZip.close()

# извлечение

#os.chdir('.\\chapter9\\')

exampleZip = zipfile.ZipFile('3.zip')
exampleZip.extractall('.\\3_from ZIP')
exampleZip.close()

#exampleZip = zipfile.ZipFile('3.zip')
#exampleZip.extract('some_text.txt')
#exampleZip.close()

# создание zip и добавление новых файлов

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('1.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()