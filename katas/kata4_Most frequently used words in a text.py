def top_3_words(text):

    def sorting_criteria(list):
        for i in list:
            if i not in counts.keys():
                counts[i] = 1
            else:
                counts[i] = counts[i] + 1
    
    def del_symbols(text):
        symbols_to_remove = [",", ".", "/", "\\", "#", ":", "//", "...", "'''", "!", "?", "_", ";", "-"]
        for symbol in symbols_to_remove:
            text = text.replace(symbol, ' ')      
        if len(text) == 1:
            text = text.replace("'", '')
        elif len(text) == 2:
            text = text.replace(" '", '')
            text = text.replace("' ", '')
        elif len(text) > 1:
            text = text.replace(" ' ", '') 
        return text

    counts = {}
    sorted_counts = {}
    top3 = []

    text = del_symbols(text)
    list = text.lower().split()

    sorting_criteria(list)
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    for k in sorted_counts.keys():
        top3.append(k)
        if len(top3) == 3:
            break
    return print(top3)

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
top_3_words("  //wont won't won't ")
top_3_words("  ...  ")
top_3_words("'")
top_3_words("' ")
top_3_words(" ' ")
top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.""")

top_3_words(" 'qiwrefj 'uzovyyebx b'whgo")