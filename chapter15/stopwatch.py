import time

print('Чтобы начать отсчет, нажмите клавишу ENTER. Впоследствии \
      для имитации щелчков мыши секундомера нажимайте клавишу <enter>. \
      для выхода из программы нажмите <ctrl + c>')

input()
print('Отсчет начат.')
start_time = time.time()

last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Замер #%s: %s (%s)' % (lap_num, total_time, lap_time), end = '')
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    # Обработать исключение <ctrl + c>, чтобы предотвратить отображение его сообщений.
    print('\nГотово')