# selenium - "эмулятор мыши"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#чтобы не закрывалось после открытия
#-----------------------------------
o = Options()
o.add_experimental_option("detach", True)
#-----------------------------------
#чтобы не закрывалось после открытия

browser = webdriver.Chrome(options=o)
print(type(browser))

browser.get('https://mail.ru/')