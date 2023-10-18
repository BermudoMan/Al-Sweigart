#! python3
# lucky.py - открывает несколько результатов поиска с помощью Google

import bs4
import requests
import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Гуглим...') # отображается при загрузке страницы Google

#res = requests.get('http://google.com/search?q=' + 'homes')
#print(res.raise_for_status())

# извлечение первых нескольких найденных ссылок
#soup = bs4.BeautifulSoup(res.text, features="html.parser")
#print(soup)
# открытие отдельной вкладки для каждого результата
#link_elems = soup.select(".srp") # не работает с динамически сгенерированными файлами

driver = webdriver.Chrome()
x = driver.get('http://google.com/search?q=' + 'homes')

link_elems = x.find_element_by_class_name('LC20lb MBeuO DKV0Md')
print(link_elems)

#num_open = min(5, len(link_elems))
#for i in range(num_open):
#    webbrowser.open('http://google.com' + link_elems[i].get('href'))