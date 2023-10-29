#! python3
# countdown.py - простой сценарий обратного отсчета

import time, subprocess

time_left = 60
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left = time_left - 1

# воспроизведение звукового файла по завершении обратного отсчета
subprocess.Popen(['start', 'alarm.wav'], shell=True)
