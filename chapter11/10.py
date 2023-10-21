# заполнение и отправка форм

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#option = webdriver.ChromeOptions()

browser = webdriver.Chrome()
browser.get('https://www.rambler.ru/')
#email_elem = browser.find_element_by_link_text('Войти в почту')
email_elem = browser.find_element_by_xpath("//a[contains(text(), 'Войти в почту')]")

email_elem.click()

#browser.maximize_window() # For maximizing window
browser.implicitly_wait(3) # gives an implicit wait for 20 seconds

email_login = browser.find_element_by_name("login")
print('Найден' + email_login)
browser.implicitly_wait(3) # gives an implicit wait for 20 seconds
email_login.click()
browser.implicitly_wait(3) # gives an implicit wait for 20 seconds
email_login.send_keys('123')
#email_password = browser.find_element_by_id("password").send_keys('12345')
#email_password.submit()
#pass