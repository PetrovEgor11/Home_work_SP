import pytest
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import cast
import requests
import json
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text
from Class_hw_10.api import api
from Class_hw_10.bd import base
import allure

bd_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients" 
base_url = 'http://5.101.50.27:8000/employee'

@allure.severity (allure.severity_level.CRITICAL)
@allure.feature("Задание № 2 из ДЗ № 10, добавление описания в API и БД запросы")
@allure.description("Тестирование получения данных")
@allure.title("Тест на проверку что первая запись с показателем first_name = Иван")
def test_get_user():
    with allure.step("Создание экземпляра класса api"):
        get_api = api()
    with allure.step("Выполнение GET запроса"):
        get_api.get_user_by_id_api
    with allure.step("Создание экземпляра класса бд"):
        get_bd = base(bd_connection_string)
    with allure.step("Выполнение Select запроса"):
        get_bd.bd_get()
    with allure.step("Сохранение результата GET запроса в переменную"):
        result_api = get_api.get_user_by_id_api()
    with allure.step("Сохранение результата Select запроса в переменную"):
        result_bd = get_bd.bd_get()
    with allure.step("Проверка что запрос БД возвращает первую строку с first_name = Иван"):
        assert result_bd['first_name'] == 'Иван'
    with allure.step("Проверка что результат БД и результат API возвращает первую строку с first_name = Иван"):
        assert result_bd['first_name'] == result_api['first_name']

@allure.severity (allure.severity_level.CRITICAL)
@allure.feature("Задание № 2 из ДЗ № 10, добавление описания в API и БД запросы")
@allure.description("Тестирование добавления данных")
@allure.title("Тест на проверку добавления пользователя через API и БД")
def test_add_new_user():
    with allure.step("Создание экземпляра класса api"):
        get_api_user = api()
    with allure.step("Вызов функции добавления пользователя через api, где сначало проверятся, что писок пользоватлей больше 1"):
        result_api = get_api_user.add_new_user_api()
    with allure.step("Создание экземпляра класса бд"):
        get_bd = base(bd_connection_string)
    with allure.step("Выполнение Select запроса"):
        before_count, after_count = get_bd.add_new_user_bd()
    with allure.step("Проверка что длина списка первого запроса select меньше, чем результа списка второго запроса select после добавления пользователя"):
        assert len(result_api['before']) < len(result_api['after'])  
    with allure.step("Проверка что количество записей в БД увеличилось на 1"):
        assert after_count == before_count + 1

@allure.severity (allure.severity_level.CRITICAL)
@allure.feature("Задание № 2 из ДЗ № 10, добавление описания в API и БД запросы")
@allure.description("Тестирование изменение данных")
@allure.title("Тест на проверку изменения данных пользователя через API")
def test_patch_user():
    with allure.step("Создание экземпляра класса api"):
        patch_api = api()
    with allure.step("Сохранение результата в переменную"):
        response = patch_api.patch_user_api()
    with allure.step("Проверка что данные изменены"):
        assert response.status_code == 200