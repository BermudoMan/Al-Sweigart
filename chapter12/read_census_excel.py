#! python3
# read_census_excel.py - форматирует таблицу данных о численности населения
# и количестве переписаных районов в каждом округе
import openpyxl, pprint
print('открытие рабочей книги')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

print('чтение строк...')
for row in range(2, sheet.max_row + 1):
    # в каждой строке содержатся данные для одного переписного района
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # гарантия существования ключа для данного штата
    county_data.setdefault(state, {})
    # гарантия существования ключа для данного округа штата
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # каждая строка представляет собой один переписной район, поэтому инкрементировать на единицу
    county_data[state][county]['tracts'] += 1
    # увеличить численность населения округа на численность населения переписного района
    county_data[state][county]['pop'] += int(pop)

# открытие нового текстового файла и запись в него содержимого словаря county_data
print('запись результатов')
result_file = open('census20xx.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('готово')