import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.test_cw_1
def test_fill_and_check_colors(driver):
    # Открытие сайта
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение полей формы
    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    button_submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()#Нажатие на кнопку Submit
    
    driver.implicitly_wait(10)#ожидание 10 сек
    
    color_zip_code = driver.find_element(By.CSS_SELECTOR, '[id="zip-code"]').value_of_css_property("color")#запрашиваем цвет элемента
    
    # color_first_name = driver.find_element(By.CSS_SELECTOR, '[id="first-name"]').value_of_css_property("color")#запрашиваем цвет элемента
    # 
    # # print(color_zip_code)
    # 
    red_backlight = "rgba(132, 32, 41, 1)" #Переменная для красной подсветки
    
    assert color_zip_code == red_backlight #Проверка
    if color_zip_code == red_backlight:
        print("Цвет элемента", '[id="zip-code"]' , "красный")
    else:
        print(print("Цвет элемента", '[id="zip-code"]', "не красный"))
        
        # green_backlight = "rgba(15, 81, 50, 1)"#Переменная для зеленой подсветки
        # # #assert '[id="first-name"]' == green_backlight
    driver.implicitly_wait(10)#ожидание 10 сек
    
    green_color_elements = [
    '[id="first-name"]', 
    '[id="last-name"]', 
    '[id="address"]', 
    '[id="city"]', 
    '[id="country"]', 
    '[id="e-mail"]', 
    '[id="phone"]', 
    '[id="job-position"]', 
    '[id="company"]'
    ]
    
    for locator in green_color_elements:
        # Находим элемент по локатору
        element = driver.find_element(By.CSS_SELECTOR, locator)
    
    # Получаем цвет элемента
    color = element.value_of_css_property("background-color")
    
    # Проверяем что цвет элемента зеленый
    if color != "rgba(15, 81, 50, 1)":
        print("Цвет элемента", locator , "зеленый")
    else:
        print("Цвет элемента", locator , "не зеленый")

