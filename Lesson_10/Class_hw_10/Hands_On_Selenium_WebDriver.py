import pytest
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import cast



class Hands:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем драйвер как переменную экземпляра

    def open_service(self):
        # Открытие сайта
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        sleep(10)

    def data_types(self):
        # Заполнение полей формы
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

        # Нажатие на кнопку Submit
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def color(self):
            
        color_zip_code = self.driver.find_element(By.CSS_SELECTOR, '[id="zip-code"]').value_of_css_property("color")#запрашиваем цвет элемента
        red_backlight = "rgba(132, 32, 41, 1)" #Переменная для красной подсветки
        
        assert color_zip_code == red_backlight #Проверка
        if color_zip_code == red_backlight:
            print("Цвет элемента", '[id="zip-code"]' , "красный")
        else:
            print(print("Цвет элемента", '[id="zip-code"]', "не красный"))
            
        self.driver.implicitly_wait(10)#ожидание 10 сек
        
        green_color_elements = [
        '[id="first-name"]', 
        '[id="last-name"]', 
        '[id="address"]', 
        '[id="city"]', 
        '[id="country"]', 
        '[id="e-mail"]', 
        '[id="phone"]', 
        '[id="job-position"]', 
        '[id="company"]'
        ]
        
        for locator in green_color_elements:
            # Находим элемент по локатору
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            
        # Получаем цвет элемента
        color = element.value_of_css_property("background-color")
        
        # Проверяем что цвет элемента зеленый
        if color != "rgba(15, 81, 50, 1)":
            print("Цвет элемента", locator , "зеленый")
        else:
            print("Цвет элемента", locator , "не зеленый")
        
    def close_driver(self):
        self.driver.quit()