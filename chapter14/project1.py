import csv, os

os.makedirs('header_removed', exist_ok=True)

for csv_file_name in os.listdir('.'):
    if not csv_file_name.endswith('.csv'):
        continue # пропустить файлы не .csv
    print('Удаление заголовка из файла ' + csv_file_name + '...')

    csv_rows = []
    csv_file_obj = open(csv_file_name)
    reader_obj = csv.reader(csv_file_obj)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue # пропустить первую строку
        csv_rows.append(row)
    csv_file_obj.close

    csv_file_obj = open(os.path.join('header_removed', csv_file_name), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()
