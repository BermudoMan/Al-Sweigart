# запись log файла

import logging

logging.basicConfig(filename='my_prog_log.txt', level=logging.DEBUG, \
                    format=' %(asctime)s - %(levelname)s - %(message)s')
