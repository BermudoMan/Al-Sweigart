import re
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP is part man, part machine, all cop.').group())

print('----------------')

names_Regex = re.compile(r'Agent \w+')
print(names_Regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))

print('----------------')
names_Regex = re.compile(r'Agent (\w)\w*')
print(names_Regex.sub(r'\1****', """Agent Alice told Agent Carol
                      that Agent Eve Knew Agent Bob was a double agent"""))

print('----------------')
