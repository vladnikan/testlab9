# test_jsonplaceholder_api.py

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. GET — получение пользователя с id=2
def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 2
    assert data["name"] == "Ervin Howell"
    assert data["email"] == "Shanna@melissa.tv"
    assert data["company"]["name"] == "Deckow-Crist" 


# 2. POST — создание нового пользователя
def test_create_user():
    payload = {
        "name": "Иван Петров",
        "job": "QA Engineer"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Иван Петров"
    assert data["job"] == "QA Engineer"
    assert "id" in data  

# 3. PUT — полное обновление пользователя
def test_update_user_put():
    payload = {
        "name": "Нео",
        "job": "The One"
    }

    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Нео"
    assert data["job"] == "The One"


# 4. DELETE — удаление пользователя (фейк, возвращает 200 и пустой JSON {})
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    assert response.text == "{}"   


