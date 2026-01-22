import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

def test_online_store(driver):
      driver.get("https://www.saucedemo.com/")
      #Авторизация
      user_name = driver.find_element(By.CSS_SELECTOR, "[id=user-name]").send_keys("standard_user")
      password = driver.find_element(By.CSS_SELECTOR, "[id=password]").send_keys("secret_sauce")
      button_login = driver.find_element(By.CSS_SELECTOR, "[id=login-button]").click()
      
      #Добавление товаров в корзину
      sauce_labs_backpack = driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-backpack]").click()
      sauce_labs_bolt = driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-bolt-t-shirt]").click()
      sauce_labs_onesie = driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-onesie]").click()
      
      #Переход в корзину
      basket = driver.find_element(By.CSS_SELECTOR, "[data-test=shopping-cart-link]").click()
      
      #Нажатие на кнопку Сheckout
      checkout = driver.find_element(By.CSS_SELECTOR, "[id=checkout]").click()
      
      #Заполнение формы Your Information
      first_name = driver.find_element(By.CSS_SELECTOR, "[id=first-name]").send_keys("Egor")
      last_name = driver.find_element(By.CSS_SELECTOR, "[id=last-name]").send_keys("Petrov")
      postal_code = driver.find_element(By.CSS_SELECTOR, "[id=postal-code]").send_keys("Moscow")
      
      button_continue = driver.find_element(By.CSS_SELECTOR, "[id=continue]").click()
      
      total = driver.find_element(By.CSS_SELECTOR, "[data-test=total-label]").text
      
      print(total)
      
      clean_total = total.replace('$', '')
      
      assert total == "Total: $58.29"
      
      if total == "Total: $58.29":
           print("Сумма равна")
      else:
          print("Сумма не равна")