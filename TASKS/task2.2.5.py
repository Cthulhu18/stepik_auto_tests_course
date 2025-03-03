from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
# используем метод execute_script для прокрутки страницы что элемент(кнопка стал видим)
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(5)
button.click()