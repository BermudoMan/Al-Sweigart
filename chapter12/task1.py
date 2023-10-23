import openpyxl
import sys


# ввод числа
if sys.argv[1] == int:
    print('Аргумент - это число')
# создание таблицы excel

wb = openpyxl.Workbook()
sheet = wb.active

x = int(sys.argv[1])

for row_ in range(1, x+1):
    for col_ in range(1, x+1):
        sheet.cell(row=row_, column=col_).value = row_*col_

# расчет содержимого ячеек
# сохранение

wb.save('task1.xlsx')



# ввод числа