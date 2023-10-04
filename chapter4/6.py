spam = ['1', '2', '2dsfsd', 'sdf']


def func(spam):
    x = ''
    for i in range(len(spam)):
        print(spam[i])
        if i < len(spam) - 1:
            x = x + (str(spam[i]) + ', ')
        else:
            x = x + ('and ' + str(spam[i]))
    print(x)

func(spam)

