import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    # Ожидание, пока цена не станет $100
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book").click()
    x_element = browser.find_element(By.ID,"input_value")
    # добавляем переменную x и присваиваем ей значение переменной x_element
    x = x_element.text
    # при помощи функции cal(x) решаем формулу на странице, ответ присваиваем перменной y
    y = calc(x)
    # записываем ответ в поле ответа
    answer = browser.find_element(By.ID,"answer").send_keys(y)
    submit = browser.find_element(By.ID,"solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
