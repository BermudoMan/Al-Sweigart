def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Переменная symbol должна быть односимвольной строкой')
    if width <= 2:
        raise Exception('Значение width должно превышать 2.')
    if height <= 2:
        raise Exception('Значение heigth должно превышать 2.')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 3), ('x', 1, 3), ('Z', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('Возникло исключение: ' + str(err))