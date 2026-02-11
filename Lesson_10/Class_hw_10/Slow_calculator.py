import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class slow_calculator:

    def __init__ (self, driver):
        self.driver = driver

    def open_service(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(45)
        
        number_7 = self.driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
        plus = self.driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
        number_8 = self.driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
        res = self.driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()
        
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), "15"))
        
        number_15 = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        assert number_15 == "15"
        
        if number_15 == "15":
            print("Результат равен 15")
        else:
            print("Результат не равен 15")
            
    def close_driver(self):
        self.driver.quit()
