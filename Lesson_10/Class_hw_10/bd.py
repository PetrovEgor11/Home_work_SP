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




class base:
    bd_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients" 
    def __init__(self, bd_connection_string):
        self.db = create_engine(bd_connection_string)
        
    # Получение данных пользователя из БД
    def bd_get(self):
        bd = create_engine(self.bd_connection_string)
        before_count = bd.execute("SELECT COUNT(*) FROM employee WHERE company_id = 2").fetchall()[0]
        
    def add_new_user_bd(self):
        bd = create_engine(self.bd_connection_string)
        bd_result_before = bd.execute("SELECT COUNT(*) FROM employee WHERE company_id = 1")
        before_count = bd_result_before.fetchone()[0]
            # Добавление пользователя через БД
        sql = text("""
        INSERT INTO employee (
            first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active
        ) VALUES (
            :first_name, :last_name, :middle_name, :company_id, :email, :phone, :birthdate, :is_active
        )
        """)
        # Тестовые данные для пользователя бд
        bd.execute(sql, {
        'first_name': "Skypro2",
        'last_name': 'Skypro2',
        'middle_name': 'Skypro2',
        'company_id': 1,
        'email': 'pe@test11.com',
        'phone': '88888888822',
        'birthdate': '2026-02-6',
        'is_active': True
    })
        bd_result_after = bd.execute(text("SELECT COUNT(*) FROM employee WHERE company_id = 1"))
        after_count = bd_result_after.fetchone()[0]
        return before_count, after_count
