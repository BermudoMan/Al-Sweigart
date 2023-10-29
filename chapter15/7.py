import threading

thread_obj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], \
                              kwargs={'sep': ' & '})
thread_obj.start()