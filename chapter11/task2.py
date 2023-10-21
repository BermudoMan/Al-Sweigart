#загрузчик изображений из интернета

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests, bs4

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1400, 900')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
browser = webdriver.Chrome(chrome_options=options)



#browser = webdriver.Chrome()

browser.get('https://imgur.com/')

browser.implicitly_wait(2)
try:
     search_line = browser.find_elements_by_xpath("//input[contains(@placeholder, 'Images, #tags, @users oh my!')]")
#     search_line.click()
     search_line.send_keys('pickles')
     print('Найден элемент <%s> с данным именем класса!' % (search_line.tag_name))
except:
     print('Не удалось найти элемент с данным именем класса.')
#browser.implicitly_wait(3) # gives an implicit wait for 20 seconds
#browser.implicitly_wait(3) # gives an implicit wait for 20 seconds
#browser.maximize_window() 
print(search_line)
#search_line.click()
#search_line.send_keys('pickles')