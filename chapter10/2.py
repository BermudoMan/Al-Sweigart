# журнал
import traceback

try:
    raise Exception('Это сообщение об ошибке.')
except:
    error_file = open('error_info.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('Информация о стеке вызовов была записана в файл error_info.txt')