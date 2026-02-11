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

class auth:

    def __init__(self, driver):
        self.driver=driver

      
    def open_service(self, driver):
        driver.get("https://www.saucedemo.com/")
    
    #Авторизация
    def auth (self, driver, user, password):
        user_name = driver.find_element(By.CSS_SELECTOR, "[id=user-name]").send_keys(user)
        password = driver.find_element(By.CSS_SELECTOR, "[id=password]").send_keys(password)
        button_login = driver.find_element(By.CSS_SELECTOR, "[id=login-button]").click()


