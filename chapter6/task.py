table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table():
    x = 0
    value_len = 0
    new_str = []
    for t in range(len(table_data) + 1):
        for i in table_data:
            if len(i[x]) > value_len:
                value_len = len(i[x])
        x += 1
    x = 0

    for t in range(len(table_data) + 1):
        for i in table_data:
            new_str.append(i[x].rjust(value_len))
        x += 1
        print(' '.join(new_str))
        new_str = []

print_table()