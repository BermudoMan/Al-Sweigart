#! python3
# lucky.py - открывает несколько результатов поиска с помощью Google

import requests, sys, webbrowser, bs4

print('Гуглим...') # отображается при загрузке страницы Google
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# извлечение первых нескольких найденных ссылок
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# открытие отдельной вкладки для каждого результата
link_elems = soup.select(' .r a')

num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))