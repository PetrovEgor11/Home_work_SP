from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")#Открытие браузера

locator_4_scr = '#landscape'#переменная для локатора

waiter = WebDriverWait(driver, 20)#Ожидание 20 сек и ожидание пока откроется 4-ая картинка 
waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, locator_4_scr))
)
locator_3_scr = '#award'#переменная для локатора

scr = driver.find_element(By.CSS_SELECTOR, locator_3_scr).get_attribute("src")#запрос инфорации по атрибуту

print(scr)#печать данных атрибута

driver.quit()#закрытие браузера