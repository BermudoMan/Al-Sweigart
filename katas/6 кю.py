def order(sentence):
    if len(sentence) > 0:
        sorted = str()
        sentence = sentence.split(' ')
        for i in range(1,10):
            for j in list(sentence):
                if str(i) in j:
                    sorted = sorted + str(j) + " "
        sorted = sorted[:-1]
        return sorted
    else:
        return ""
    
order("4of Fo1r pe6ople g3ood th5e the2")
#print(type(order("4of Fo1r pe6ople g3ood th5e the2")))
#print(type(sorted))