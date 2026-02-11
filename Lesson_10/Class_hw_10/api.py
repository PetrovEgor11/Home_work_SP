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



class api:
    def __init__(self):
        self.base_url = 'http://5.101.50.27:8000/employee'


    # Тест, получение данных о пользователе по ID
    def get_user_by_id_api(self):
        # Получение данных пользователя через GET запросу API
        get_api = requests.get(self.base_url + '/info/1')
        assert get_api.status_code == 200
        return get_api.json()
        
    # Тест добавления пользователя
    def add_new_user_api(self):
        # Проверка кол-во записей до добавления пользователей через API
        get_api_user = requests.get(self.base_url + '/list/1')
        assert get_api_user.status_code == 200
        users_before = get_api_user.json()  # Сохраняем данные
        # Добавление пользователя через API
        add_new_user = {
            "first_name": "Skypro",
            "last_name": "Skypro",
            "middle_name": "Skypro",
            "company_id": 1,
            "email": "Skypro@test.com",
            "phone": "88888888888",
            "birthdate": "2026-02-06",
            "is_active": True
            }
        response_after = requests.post(self.base_url + '/create', json=add_new_user)
        assert response_after.status_code == 200

        return {
            'before': users_before,
            'after': response_after.json()
        }
        
    # Тест по изменению пользователя
    def patch_user_api(self):
        # Получение токена
        params = {
            "username": "harrypotter",
            "password": "expelliarmus"
            }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        get_token = requests.post('http://5.101.50.27:8000/auth/login', json=params, headers=headers)
        assert get_token.status_code == 200
        token = get_token.json()["user_token"] 
        
        
        params_patch_user = {
            "last_name": "SkyPro-Patch",
            "email": "SkyPro-Patch@example.com",
            "phone": "88888888888",
            "is_active": True
            }
        info_user = {
            'employee_id' : "1",
            'client_token' : token
            }
        # Изменение пользователя
        patch_user = requests.patch(self.base_url + 'change', json=params_patch_user, headers=info_user)
        assert patch_user.status_code == 200
        return patch_user