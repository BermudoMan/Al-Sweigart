from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)

url = 'https://vk.com'

try:
    driver.get(url=url)
    time.sleep(5)

    email_input = driver.find_element(By.XPATH, "//input[@id='index_email']")
    email_input.clear()
    email_input.send_keys("79433422")
    time.sleep(3)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span[class='FlatButton__in']")
    login_button.click()
    print("Test passed: click on button ")
    time.sleep(3)

    assert_value = driver.find_element(By.CSS_SELECTOR,".vkuiFormItem__bottom.vkuiCaption.vkuiCaption--l-1").text
    assert assert_value == "Incorrect phone number [1000]"
    print("Test assert: Сверяет значение ошибки на странице" )

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()