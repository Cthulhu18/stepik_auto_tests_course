from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Извлечение значений из элементов
    num1 = int(browser.find_element(By.ID,"num1").text)
    num2 = int(browser.find_element(By.ID,"num2").text)
    sum_result = num1 + num2
    # Находим элемент <select>
    select_element = browser.find_element(By.ID,"dropdown")
    # Создаем объект Select
    select = Select(select_element)
    select.select_by_value(str(sum_result))  # Преобразуем сумму в строку, так как value всегда строка
    submit = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

