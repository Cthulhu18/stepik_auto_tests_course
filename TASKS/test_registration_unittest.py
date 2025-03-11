import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Заполняем обязательные поля
        self.browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]").send_keys("Ivan")
        self.browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]").send_keys("Ivanov")
        self.browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]").send_keys("ivan182@mail.ru")

        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем результат
        success_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(success_text, "Congratulations! You have successfully registered!", "Registration failed")

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Заполняем обязательные поля
        self.browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]").send_keys("Ivan")
        self.browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]").send_keys("Ivanov")
        self.browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]").send_keys("ivan182@mail.ru")

        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем результат
        success_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(success_text, "Congratulations! You have successfully registered!", "Registration failed")


if __name__ == "__main__":
    unittest.main()