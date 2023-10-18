from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome()
browser.get('https://xkcd.com/')

try:
     elem = browser.find_element_by_id('comic')
     print('Найден элемент <%s> с данным именем класса!' % (elem.tag_name))
except:
     print('Не удалось найти элемент с данным именем класса.')