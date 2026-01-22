from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login") #Открыть сайт

Username_locator = '[id=username]' #Присвоили локутору "Username"переменную

Username_input=driver.find_element(By.CSS_SELECTOR, Username_locator) #Сделали поиск латора и так же присвоили переменную для поиска локатора

Username_input.send_keys("tomsmith") #Просим написать в локатор, а именно в строку Username "tomsmith"

Password_locator = '[id=password]' #Присвоили локутору поля "Password" переменную

Password_input=driver.find_element(By.CSS_SELECTOR, Password_locator) #Сделали поиск латора и так же присвоили переменную для поиска локатора

Password_input.send_keys("SuperSecretPassword!") #Просим написать в локатор, а именно в строку Password "SuperSecretPassword"

Button_login_locator = '[type=submit]' #Присвоили локутору "Login"переменную

Button_login_locator=driver.find_element(By.CSS_SELECTOR, Button_login_locator) #Сделали поиск латора и так же присвоили переменную для поиска локатора

Button_login_locator.click() #Просим нажать на кнопку "Login"

sleep(3)