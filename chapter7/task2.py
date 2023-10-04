import re

def y(string, x):
    if len(x) == 0:
        del_space = re.sub(r'(^\W+)|(\W+$)', '', string)   
        print(del_space)
    else:
        del_space = re.sub(x, '', string)
        print(del_space)
y('     Alice saw owl!   ', r'[l]')