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

driver.get("https://www.uitestingplayground.com/progressbar")



driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter = WebDriverWait(driver, 40, 0.1) #методу wait присовили перменную, на вход принимает дрвйвер и 40 сек задержки, третьим на вход идет как часто мы хотим запрашивать инфу от сайта
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%") #просим методом until (ждать пока что-то произойдет) 
    #элемент по локатору сообщить нам, когда будет вывдеено 75%
    )

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print(driver.find_element(By.CSS_SELECTOR, "#result").text)

driver.quit


# until - ждать пока что-то произойдет 
# until not - не ждать пока что-то произойдет