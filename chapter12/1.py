import openpyxl
import os

x = os.getcwd()
os.chdir(x + '//chapter12')
print(os.getcwd())

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Лист3')
print(sheet)
print(type(sheet))
print(sheet.title)

another_sheet = wb.get_active_sheet()
print(another_sheet)