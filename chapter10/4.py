#имитация работы светофора

#перекрестки
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'green', 'ew': 'red'}

def switch_lights(stoplights):
    for key in stoplights.keys():
        if stoplights[key] == 'green':
            stoplights[key] = 'yellow'
        elif stoplights[key] == 'yellow':
            stoplights[key] = 'red'
        elif stoplights[key] == 'red':
            stoplights[key] = 'green'

    assert 'red' in stoplights.values(), 'Ни один из сигналов не является красным!' + str(stoplights)
switch_lights(market_2nd)

# python -O *.py - отключение утверждений