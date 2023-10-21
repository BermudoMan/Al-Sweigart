from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests, bs4
import random

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1400, 900')

browser = webdriver.Chrome(chrome_options=options)

browser.get('https://gabrielecirulli.github.io/2048/')


try:
    elem = browser.find_element_by_xpath('/html/body')
    print('Все хорошо')
except:
    print('Все плохо')
browser.implicitly_wait(5)

while True:
    x = random.randint(1, 4)
    print(x)
    if x == 1:
        elem.send_keys(Keys.ARROW_DOWN)
    elif x == 2:
        elem.send_keys(Keys.ARROW_LEFT)
    elif x == 3:
        elem.send_keys(Keys.ARROW_RIGHT)
    elif x == 4:
        elem.send_keys(Keys.ARROW_UP)

