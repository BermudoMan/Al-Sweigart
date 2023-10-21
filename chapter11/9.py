# клик мышью
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome()
browser.get('https://inventwithpython.com/')

link_elem = browser.find_element_by_link_text('Free link #2')

print(type(link_elem))

link_elem.click()