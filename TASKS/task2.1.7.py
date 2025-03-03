import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # находим значение x на странице и присваиваем его переменной x_element
    x_element = browser.find_element(By.ID,"treasure")
    # добавляем переменную x и присваиваем ей значение переменной x_element
    x = x_element.get_attribute("valuex")
    # при помощи функции cal(x) решаем формулу на странице, ответ присваиваем перменной y
    y = calc(x)
    # записываем ответ в поле ответа
    answer = browser.find_element(By.ID,"answer").send_keys(y)
    chekbox = browser.find_element(By.ID,"robotCheckbox").click()
    radiobatton = browser.find_element(By.ID,"robotsRule").click()
    submit = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
