from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/visibility")# переход на сайт

sleep(5)

locator_opasity_0 = "[id=transparentButton]"

is_displayed_opasity_0 = driver.find_element(By.CSS_SELECTOR, locator_opasity_0).is_displayed() #проверка видимости элемента
print(is_displayed_opasity_0)

locator_hide = "[id=hideButton]"

hide = driver.find_element(By.CSS_SELECTOR, locator_hide).click() #нажмаем на кнопку после которой элекмент пропадает из видимости

is_displayed_opasity_0 = driver.find_element(By.CSS_SELECTOR, locator_opasity_0).is_displayed()#для проверки, видим ли элемент на текущей веб-странице.
print(is_displayed_opasity_0)

hide = driver.find_element(By.CSS_SELECTOR, locator_hide).is_selected() #используется для проверки состояния выбранности элемента
print(hide)

hide = driver.find_element(By.CSS_SELECTOR, locator_hide).is_enabled() #используется для проверки, доступен ли элемент для взаимодействия с пользователем
print(hide)
