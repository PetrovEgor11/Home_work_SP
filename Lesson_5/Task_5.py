from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def click_blue_button():
    driver = webdriver.Chrome()  # создаем новый драйвер
    driver.get("http://uitestingplayground.com/classattr")
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    sleep(3)
    driver.quit()

# Запускаем 3 раза
for i in range(3):
    print(f"Итерация {i+1}")
    click_blue_button()
