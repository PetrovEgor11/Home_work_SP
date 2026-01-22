from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome
driver_chrome = webdriver.Chrome()
driver_chrome.get("https://uitestingplayground.com/dynamicid")
sleep(2)
driver_chrome.find_element(By.CSS_SELECTOR, '.btn-primary').click()
sleep(2)
driver_chrome.quit()

# Firefox  
driver_firefox = webdriver.Firefox()
driver_firefox.get("https://uitestingplayground.com/dynamicid")
sleep(2)
driver_firefox.find_element(By.CSS_SELECTOR, '.btn-primary').click()
sleep(2)
driver_firefox.quit()



