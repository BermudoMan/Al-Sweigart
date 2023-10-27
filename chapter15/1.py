import time
import sys
sys.set_int_max_str_digits(0)

print(time.time())


def calc_prod():
    # вычисление произведения первых 100000 чисел
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


start_time = time.time()
prod = calc_prod()
end_time = time.time()
print('Длина результата: %s цифр' % (len(str(prod))))
print('Расчет занял %s секунд.' % (end_time - start_time))
