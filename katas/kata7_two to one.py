def longest(a1, a2):
    final = []
    f = ''
    full = a1 + a2
    full_sorted = list(full)
    full_sorted.sort()
    for i in full_sorted:
        if i not in final:
            final.append(i)
    for j in final:
        f += j

    return f

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
