import re

ha_Regex = re.compile(r'(Ha){3}')
print(ha_Regex.search('HaHaHa').group())
try:
    print(ha_Regex.search('Ha').group())
except:
    print('None')

print('--------------1')

greedy_Ha = re.compile(r'(Ha){3,5}')
print(greedy_Ha.search('HaHaHaHaHa').group())
greedy_Ha = re.compile(r'(Ha){2,5}?')
print(greedy_Ha.search('HaHaHaHaHa').group())

print('--------------2')

phone_num_Regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phone_num_Regex.search("""Сотовый: 415-555-2134. 
                             Рабочий: 241-233-2211""").group())
print(phone_num_Regex.findall("""Сотовый: 415-555-2134. 
                             Рабочий: 241-233-2211"""))

phone_num_Regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phone_num_Regex.findall("""Сотовый: 415-555-2134. 
                             Рабочий: 241-233-2211"""))