def spin_words(sentence):
    sentence2 = ''
    sentence = sentence.split(' ')
    for i in sentence:
        if len(i) >= 5:
            rev = i[::-1]
            sentence2 = sentence2 + rev + ' '
        elif len(i) < 5:
            sentence2 = sentence2 + i + ' '
    sentence2 = sentence2[:-1]
    print(sentence2)
    return sentence2



spin_words('Hey fellow warriors')