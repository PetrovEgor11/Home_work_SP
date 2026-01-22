from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")# переход на сайт

#element = driver.find_element(By.CSS_SELECTOR, '#text') # поиск локатора на сайте
#session="8d2a37d27545a1f1511c9ca74b6a4a00", element="f.379AF3B1492ECC97D7C15631CECE0C97.d.1A59D5E96D9E113C81C099C762BB0C38.e.8"

#element.clear() #очистить поле
#print(element) #Напечатать элементы
#driver.find_elements()#Найти элементы
#element.send_keys("test") #вписать текст в локатор

#button_search = "[aria-label=Найти]"

#button_search = driver.find_element(By.CSS_SELECTOR, button_search)

#button_search.click()



Wait_locator = '[data-statlog="2informers.weather"]' # локатор по погоде на яндексе

Wait_locator = driver.find_element(By.CSS_SELECTOR, Wait_locator) # поиск локатора на странице
txt = Wait_locator.text #переменная для текста локатора 
print(txt) #напечтать текст в локаторе 

id = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.weather"]').id #запрашиваем id элемента
print(id)#печатаем id элемента

href = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.weather"]').get_attribute("href")

print(href)

css = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.weather"]').value_of_css_property("front_family")#запрашиваем css элементы значения

print(css)

color = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.weather"]').value_of_css_property("color")#запрашиваем цвет элемента

print(color)

sleep(10)
driver.quit()#Закрыть браузер
