spam = '  Hello world! '
#убирает пробельные символы справа и слева
print(spam.strip())
print(spam.strip())
print(spam.strip('!'))
print(spam.strip('  Hel'))
print(spam.strip('  leH'))
print(spam.strip('  lH'))
print(spam.strip('  eH'))
print(spam.strip('! '))