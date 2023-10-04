#классы символов

import re

xmas_Regex = re.compile(r'\d+\s\w+')
print(xmas_Regex.findall("""12 drummers, 11 pipers, 10 lords, 9 ladies
                         8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves,
                         1 partridge"""))
print('--------------1')

#свой класс символов

vowel_Regex = re.compile(r'[aeiouAEIOU]')
print(vowel_Regex.findall('RoboCop eats baby food. BABY FOOD'))
print('--------------2')

vowel_Regex = re.compile(r'[^aeiouAEIOU]')
print(vowel_Regex.findall('RoboCop eats baby food. BABY FOOD'))

print('--------------3')
vowel_Regex = re.compile(r'^RoboCop')
print(vowel_Regex.search('RoboCop eats baby food. BABY FOOD'))
try:
    print((vowel_Regex.search('Hui eats baby food. BABY FOOD')))
except:
    print('None')

print('--------------3')
vowel_Regex = re.compile(r'\d$')
print(vowel_Regex.search('Your number is 42'))
try:
    print(vowel_Regex.search('Your number is forty two'))
except:
    print('None')

print('--------------4')

vowel_Regex = re.compile(r'^\d+$')
print(vowel_Regex.search('1234567890'))
print(vowel_Regex.search('12345xyz67890'))
print(vowel_Regex.search('12 34567890'))

#групповой символ
print('--------------5')
vowel_Regex = re.compile(r'.at')
print(vowel_Regex.findall('The cat in the hat sat on the flat mat'))
vowel_Regex = re.compile(r'..at')
print(vowel_Regex.findall('The cat in the hat sat on the flat mat'))

print('--------------6')

vowel_Regex = re.compile(r'First Name: (.*) Last Name: (.*)')

print(vowel_Regex.search('First Name: Al Last Name: Sweigart').group(1))
print(vowel_Regex.search('First Name: Al Last Name: Sweigart').group(2))

#нежадный поиск
vowel_Regex = re.compile(r'<.*?>')
print(vowel_Regex.search('<To serve man> for dinner.>').group())
vowel_Regex = re.compile(r'<.*>')
print(vowel_Regex.search('<To serve man> for dinner.>').group())

print('--------------7')
vowel_Regex = re.compile(r'.*')
print(vowel_Regex.search("Serve the public trust. \nProtect the innocent.\nUphold the low").group())
print('________')
vowel_Regex = re.compile(r'.*', re.DOTALL)
print(vowel_Regex.search("Serve the public trust. \nProtect the innocent.\nUphold the low").group())



