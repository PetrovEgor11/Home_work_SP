from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver_chrome.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
button_close = driver_chrome.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p")
button_close.click()
sleep(3)


driver_firefox.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
button_close = driver_firefox.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p")
button_close.click()
sleep(3)


