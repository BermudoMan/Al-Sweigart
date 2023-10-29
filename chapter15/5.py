import datetime

oct21str = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21str.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21str.strftime('%I:%M %p'))
print(oct21str.strftime("%B of '%y"))

# преобразование строк в объекты datetime

print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))