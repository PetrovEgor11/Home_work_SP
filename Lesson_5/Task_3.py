from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



def browser(driver):
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/") #Открыть сайт

    Add_Element_locator = 'button' #Присвоили локутору "Add_Element" переменную

    serch_Add_Element_locator = driver.find_element(By.CSS_SELECTOR, Add_Element_locator)#Поиск локатора "Add_Element" на сайте

    for x in range(5):
        serch_Add_Element_locator.click()#5 раз кликнуть на кнопку "Add Element"

    delete_locator = '.added-manually'#Присволи локатору "Delete" переменную

    delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_locator) #Поиск локатора "Delete" на сайте

    print (len(delete_buttons)) #Вывод размера списка 

    sleep(10) #Задержка на 10 сек


chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

browser(chrome)
browser(firefox)


