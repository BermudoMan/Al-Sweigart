def duplicate_count(text):
    f = []
    x = text.lower()
    for i in x:
        counter = x.count(i)
        if counter > 1 and i not in f:
            f.append(i)
    return print(len(f))

duplicate_count('ndfssgf')

