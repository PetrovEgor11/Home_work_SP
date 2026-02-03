import requests
import json
from sqlalchemy import create_engine, inspect
import pytest
from sqlalchemy.sql import text

base_url = 'http://5.101.50.27:8000/employee'
db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


# Тест, получение данных
def test_get_user():
    # Проверяем, что API возвращает 200
    get_API = requests.get(base_url + '/info/1')
    assert get_API.status_code == 200
    
    # Проверяем БД отдельно
    db = create_engine(db_connection_string)
    db_result = db.execute("SELECT * FROM employee WHERE id = 1").fetchall()





# Тест, добаление нового пользователя
def test_add_new_user():
    # Атрибуты нового пользователя
    new_user = {
        "first_name": "Egor",
        "last_name": "Petrov",
        "middle_name": "Дмитриевич",
        "company_id": 1,
        "email": "pe@test.com",
        "phone": "88888888888",
        "birthdate": "2026-01-27",
        "is_active": True
    }

    # Отправка POST-запроса на создание пользователя
    response = requests.post(base_url +'/create', json=new_user)
    assert response.status_code == 200
    user_data = response.json()

    # Подключение к БД
    db = create_engine(db_connection_string)
    sql = text("""
        INSERT INTO employee (
            first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active
        ) VALUES (
            :first_name, :last_name, :middle_name, :company_id, :email, :phone, :birthdate, :is_active
        )
    """)
    db.execute(sql, {
        'first_name': "Egor2.0",
        'last_name': 'Petrov2.0',
        'middle_name': 'Дмитриевич2.0',
        'company_id': 1,
        'email': 'pe@test11.com',
        'phone': '88888888822',
        'birthdate': '2026-01-27',
        'is_active': True
    })