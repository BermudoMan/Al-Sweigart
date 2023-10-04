def friend(x):
    for i in x:
        if len(i) > 4:
            x.remove(i)
            return print(x)
        elif len(i) < 4:
            x.remove(i)
            return print(x)


friend(["Ryan", "Jimmy", "123", "4", "Cool Man"])