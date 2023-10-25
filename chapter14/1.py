import csv

example_file = open('example.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
#print(example_data)
print(example_data[0][0])

for row in example_data:
#    print('Строка #' + str(example_reader.line_num) + ' ' + str(row))
    print('Строка #' + str(example_reader.line_num) + ' ' + str(row))


output_file = open('output.csv', 'w', newline='')
output_writter = csv.writer(output_file)
output_writter.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writter.writerow(['1', '2', '3.14423', '4'])
output_file.close()

output_file2 = open('output2.tsv', 'w', newline='')
output_writter = csv.writer(output_file2, delimiter='\t', lineterminator='\n\n')
output_writter.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writter.writerow(['1', '2', '3.14423', '4'])
output_file2.close()