import requests
import json
from sqlalchemy import create_engine, inspect
import pytest
from sqlalchemy.sql import text

base_url = 'http://5.101.50.27:8000/employee'
bd_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


# Тест, получение данных о пользователе по ID
def test_get_user_by_id():
    # Получение данных пользователя через GET запросу API
    get_API = requests.get(base_url + '/info/1')
    assert get_API.status_code == 200
    result_api = get_API.json()
    
    
    # Получение данных пользователя из БД
    bd = create_engine(bd_connection_string)
    bd_result = bd.execute("SELECT * FROM employee WHERE id = 1").fetchall()
    row_1 = bd_result[0]
    assert row_1['first_name'] == 'Иван'
    assert row_1['first_name'] == result_api['first_name']

# Тест добавления пользователя
def test_add_new_user():
    # Проверка кол-во записей до добавления пользователей через API
    Get_API = requests.get(base_url + '/list/1')
    response_api = Get_API.json()
    assert len(response_api) > 1
    # Проверка кол-во записей до добавления пользователей через БД
    bd = create_engine(bd_connection_string)
    bd_result = bd.execute("SELECT * FROM employee where company_id = 2").fetchall()
    assert len(bd_result) > 1

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
    add_new_user = requests.post(base_url +'/create', json=add_new_user)
    assert add_new_user.status_code == 200
    
    # Добавление пользователя через БД
    sql = text("""
        INSERT INTO employee (
            first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active
        ) VALUES (
            :first_name, :last_name, :middle_name, :company_id, :email, :phone, :birthdate, :is_active
        )
    """)
    # Тестовые данные для пользователя 2 
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
    # Проверка увеличения списка пользователей после добавления 2-ух пользователей 
    assert len(response_api) + 2
    assert len(bd_result) + 2


# Тест по изменению пользователя
def test_patch_user():
    # Плучение токена
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
    patch_user = requests.patch(base_url + 'change', json=params_patch_user, headers=info_user)
    assert patch_user.status_code == 200
