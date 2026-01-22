from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")# переход на сайт

element = driver.find_element(By.CSS_SELECTOR, '#text') # поиск локатора на сайте
#session="8d2a37d27545a1f1511c9ca74b6a4a00", element="f.379AF3B1492ECC97D7C15631CECE0C97.d.1A59D5E96D9E113C81C099C762BB0C38.e.8"
element.send_keys("test") #вписать текст в локатор
element.clear() #очистить поле
#print(element) #Напечатать элементы
#driver.find_elements()#Найти элементы

sleep(10)
driver.quit()#Закрыть браузер

