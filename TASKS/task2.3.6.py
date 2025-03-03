import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # WebDriverWait(browser, 10).until(EC.alert_is_present())
    new_window = browser.window_handles[1]
    confirm = browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID,"input_value")
    # добавляем переменную x и присваиваем ей значение переменной x_element
    x = x_element.text
    # при помощи функции cal(x) решаем формулу на странице, ответ присваиваем перменной y
    y = calc(x)
    # записываем ответ в поле ответа
    answer = browser.find_element(By.ID,"answer").send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()