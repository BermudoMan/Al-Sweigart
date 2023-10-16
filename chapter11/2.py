import requests

#res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Google_Maps_icon_%282020%29.svg/1200px-Google_Maps_icon_%282020%29.svg.png')

print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text)

print('-------------')
res2 = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print(res2.text[:250])
print(res.raise_for_status()) #проверка после загрузки (get)
print(res2.raise_for_status())


