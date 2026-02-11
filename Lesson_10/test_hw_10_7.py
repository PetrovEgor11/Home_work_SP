import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from Class_hw_10.Hands_On_Selenium_WebDriver import Hands
from Class_hw_10.Slow_calculator import slow_calculator
from Class_hw_10.Page_add_basket import add_basket
from Class_hw_10.Page_basket import page_basket
from Class_hw_10.Page_auth import auth
from Class_hw_10.Page_Your_information import Your_information



@allure.severity (allure.severity_level.CRITICAL)
@allure.feature("Задание № 1 из ДЗ № 7, добавление описания")
@allure.description("Тестирование формы данных")
@allure.title("Тест на проверку цвета элементов формы")
def test_hw_10_hands_on_selenium_webdriver():
    with allure.step("Создание драйвера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    with allure.step("Создание экземпляра класса Hands"):
        page_hands = Hands(driver)
    
    with allure.step("Открытие сервиса"):
        page_hands.open_service()
    
    with allure.step("Заполнение формы данными"):
        page_hands.data_types()
    
    with allure.step("Проверка цвета элементов"):
        page_hands.color()
    
    with allure.step("Закрытие драйвера"):
        page_hands.close_driver()

@allure.severity (allure.severity_level.CRITICAL)
@allure.feature("Задание № 2 из ДЗ № 7, добавление описания")
@allure.description("Тестирование калькулятора")
@allure.title("Тест на проверку выдачи корректно результата по итогам определенного времени")
def test_calculator():
    with allure.step("Создание драйвера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание экземпляра класса"):
        calculator = slow_calculator(driver)
    with allure.step("Заполнение формы данными (на калькуляторе 7+8)и проверка (через 45 секунд отобразится результат 15)"):
        calculator.open_service()
    with allure.step("Закрытие драйвера"):
        calculator.close_driver()

@allure.severity (allure.severity_level.CRITICAL)
@allure.feature("Задание № 3 из ДЗ № 7, добавление описания")
@allure.description("Тестирование интернет-магазинa")
@allure.title("Тест на проверку авторизации, добавления товаров корзину, заполнение контактной инфомрации и проверку стоимости товаров в корзине")
def test_saucedemo():
    with allure.step("Создание драйвера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Создание экземпляра класса auth"):
        auth_page = auth(driver)
    with allure.step("Открытие веб-страницы интренет магазина"):
        auth_page.open_service(driver)
        with allure.step("Авторизация, заполнение поля Username и Password"):
            auth_page.auth(driver, "standard_user", "secret_sauce")

    with allure.step("Создание экземпляра класса add_basket"):
        add_basket_product = add_basket(driver) 
        with allure.step("Добавление товаров в корзину"):
            add_basket_product.put_products()

    with allure.step("Создание экземпляра класса page_basket"):
        page_basket_product = page_basket(driver)
        with allure.step("Откртие страницы корзины"):
            page_basket_product.open_basket()
 
    with allure.step("Создание экземпляра класса Your_information"):
        page_your_information = Your_information(driver)
        with allure.step("Заполняем данные о доставке: First Name, Last Name, Zip/Postal Code"):
            page_your_information.page_your_information(driver, "Egor", "Petrov", "Moscow")
            sleep (10)
        with allure.step("Проверка результата, что сумма товара соответствует"):
            page_your_information.result()
        with allure.step("Закрытие браузера"):
            page_your_information.close_driver()



