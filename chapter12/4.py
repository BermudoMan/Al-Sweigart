#выполнение преобразований между буквенными и цифровыми обозначениями столбцов
import openpyxl


wb = openpyxl.load_workbook('example.xlsx')
#sheet = wb.get_sheet_by_name('Лист1')

sheet = wb.active

print(sheet['B'])
for cell_obj in sheet['B']:
    print(cell_obj.value)
