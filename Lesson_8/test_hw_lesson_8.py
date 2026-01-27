import requests
import json

base_url = 'http://5.101.50.27:8000/employee'

# Тест, добаление нового пользователя
def test_add_new_user():
    #Атрибуты новой сущности
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
    #Добавление новой сущности (компании)
    adn = requests.post(base_url +'/create', json=new_user)
    assert adn.status_code == 200
    user_data = adn.json()



# Тест, получение данных о пользователе
def test_get_user():
    employee_id = 10
    get_info_user = requests.get(base_url + '/info/10', json=employee_id)
    assert get_info_user.status_code == 200

# Тест, получение данных о сотрудниках компании
def test_get_user_in_company():
    company_id = 1
    get_info_user = requests.get(base_url + '/list/1', json=company_id)
    assert get_info_user.status_code == 200

def test_patch_user():
    new_user = {
         "first_name": "Egor1",
         "last_name": "Petrov1",
         "middle_name": "Дмитриевич1",
         "company_id": 1,
         "email": "pe@test.com",
         "phone": "88888888888",
         "birthdate": "2026-01-27",
         "is_active": True
        } 
    adn = requests.post(base_url +'/create', json=new_user)
    assert adn.status_code == 200
    user_data = adn.json()
    edit_user = {
         "last_name": "Petrov11",
         "email": "pe11@test.com",
         "phone": "88888888811",
         "is_active": True
        } 
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJyeXBvdHRlciIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc2OTUzNTY3MX0.tbdFAaRHVQqLjxIblRsWs6qDiiw5zPJ8jPZDtUcuimw"
    }
    adn = requests.patch(base_url +'/change', json=edit_user, headers=headers)
    assert adn.status_code == 200
    


