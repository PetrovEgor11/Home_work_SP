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


class Your_information:

    def __init__(self, driver):
        self.driver = driver

    #Заполнение формы Your Information
    def page_your_information(self, driver, first_name, last_name, address):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "[id=first-name]").send_keys(first_name)
        last_name = self.driver.find_element(By.CSS_SELECTOR, "[id=last-name]").send_keys(last_name)
        postal_code = self.driver.find_element(By.CSS_SELECTOR, "[id=postal-code]").send_keys(address)
        button_continue = self.driver.find_element(By.CSS_SELECTOR, "[id=continue]").click()

        #Проверка 
    def result (self):
        total = self.driver.find_element(By.CSS_SELECTOR, "[data-test=total-label]").text   
        print(total)      
        clean_total = total.replace('$', '')
        assert total == "Total: $58.29"

    def close_driver(self):
        self.driver.quit()
