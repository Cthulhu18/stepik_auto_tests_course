from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    
    alert('Hello!');
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, "test.txt")
    # browser.get(link)
    # first_name = browser.find_element(By.NAME,"firstname").send_keys("Sergey")
    # last_name = browser.find_element(By.NAME,"lastname").send_keys("Makhno")
    # email = browser.find_element(By.NAME,"email").send_keys("test182@.mail.ru")
    # upload_file = browser.find_element(By.ID,"file").send_keys(file_path)
    # submit_btn = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
