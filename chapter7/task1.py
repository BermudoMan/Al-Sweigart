import re

def password_check():
    password = input()
    check = re.compile(r'''(?=.*[0-9_].*)(?=.*[a-z_].*)(?=.*[A-Z_].*)[0-9a-zA-Z_]{8,}$''')
    try:
        check.search(password).group()
        print('Good password')
    except:
        print('Weak password')

password_check()