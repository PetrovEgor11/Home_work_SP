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

driver.get("http://uitestingplayground.com/ajax") #Откртые браузера


blue_button = '#ajaxButton' #переменная для локатора

blue_button = driver.find_element(By.CSS_SELECTOR, blue_button).click() #нажатие на локатор

driver.implicitly_wait(16) #ожидаем 16 сек

#content_locator = '#content'

#content_locator = driver.find_element(By.CSS_SELECTOR, content_locator)

content_text = ".bg-success"#переменная для локатора

text = driver.find_element(By.CSS_SELECTOR, content_text).text#вывести текст локатора

txt = text

print(txt)#напечатать текст

driver.quit()#закрыть браузер

