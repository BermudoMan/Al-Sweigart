import requests, bs4

res = requests.get('http://nostarch.com')
print(res.raise_for_status())
no_starch_soup = bs4.BeautifulSoup(res.text)
print(type(no_starch_soup))

print('========')
