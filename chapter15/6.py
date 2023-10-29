# многопоточность

import threading, time
print('Начало программы')

def take_anap():
    time.sleep(15)
    print('Проснись!')

thread_obj = threading.Thread(target=take_anap)
thread_obj.start()
print('Конец программы.')