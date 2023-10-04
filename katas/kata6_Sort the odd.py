def sort_array(source_array):
    sorted_source = []
    indexes = []
    ind = 0
    for i in source_array:
        if i % 2 != 0:
            sorted_source.append(i)
        sorted_source.sort()
        if i % 2 == 0:
            indexes.append(ind)
        ind += 1
    for j in indexes:
        sorted_source.insert(j, source_array[j])



    return print(sorted_source, indexes)


sort_array([1, 3, 2, 8, 5, 4])