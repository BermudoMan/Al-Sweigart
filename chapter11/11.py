# заполнение и отправка форм

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://www.google.ru/?hl=ru')
browser.maximize_window() # For maximizing window
elem = browser.find_element_by_id('APjFqb')
#elem.click()
elem.send_keys('12312')
elem.send_keys(Keys.ENTER)

