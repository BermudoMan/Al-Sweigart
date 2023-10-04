x = {}
if 'color' not in x:
    x['color'] = 'black'
print(x)

x.setdefault('weight', 345)
print(x)
x.setdefault('weight', 221)
print(x)