#! python3
# project2 - выводит прогноз погоды для заданного населенного пункта (долгота\широта)
import requests
import json
import sys

# Определение название населенного пункта из аргументов командной строки
if len(sys.argv) < 2:
    print('Использование: project2 location')
    sys.exit()
longitude = sys.argv[1]
latitude = sys.argv[2]

# загрузить данные json из API сайта OpenWeatherMap.org.
url = 'https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%d&hourly=temperature_2m&forecast_days=1' \
    % (float(longitude), float(latitude))

responce = requests.get(url)
responce.raise_for_status()

# загрузка json в переменную python
weather_data = json.loads(responce.text)
print(weather_data)