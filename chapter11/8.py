from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="Z:\\webdrivers\\chrome-win64\\chrome.exe")
options = webdriver.ChromeOptions()

options.binary_location = "Z:\\webdrivers\\chrome-win64\\chrome.exe"
driver = webdriver.Chrome(service=service, options=options)

#browser = webdriver.Chrome()
browser.get('https://xkcd.com/')

try:
     elem = browser.find_element_by_id('comic')
     print('Найден элемент <%s> с данным именем класса!' % (elem.tag_name))
except:
     print('Не удалось найти элемент с данным именем класса.')