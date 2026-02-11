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

class add_basket:

    def __init__(self, driver):
        self.driver = driver
    
    #Добавление товаров в корзину
    def put_products(self):
        sauce_labs_backpack = self.driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-backpack]").click()
        sauce_labs_bolt = self.driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-bolt-t-shirt]").click()
        sauce_labs_onesie = self.driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-onesie]").click()