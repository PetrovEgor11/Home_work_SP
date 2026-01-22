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

driver.get("http://uitestingplayground.com/textinput") #открыть браузер 


my_button = '#newButtonName'#переменная для локатора

serch_my_button = driver.find_element(By.CSS_SELECTOR, my_button)#поиск локатора на странице

serch_my_button.send_keys("SkyPro")#вписать текст в поле


blue_button = '#updatingButton'#переменная для локатора

serch_blue_button = driver.find_element(By.CSS_SELECTOR, blue_button).click()#нажать на локатор


driver.implicitly_wait(10)#ожидание 10 сек

text = driver.find_element(By.CSS_SELECTOR, blue_button).text#запрос текста локатора

txt = text

print(txt)#напечатать текст локатора

driver.quit()#закрытие браузера
