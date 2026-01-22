from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs") #Открыть сайт

serch_locator = '[type=number]' #Присвоили локутору переменную

serch_input=driver.find_element(By.CSS_SELECTOR, serch_locator) #Сделали поиск латора и так же присвоили переменную для поиска локатора

serch_input.send_keys("1000") #Просим написать в локатор, а именно в строку поиска "1000"
sleep(3)

serch_input.clear() #Очищаем строку 

sleep(3)

serch_input.send_keys("999") #Просим написать в локатор, а именно в строку поиска "999"

sleep(3)