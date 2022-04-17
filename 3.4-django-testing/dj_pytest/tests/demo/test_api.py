import pytest
from rest_framework.test import APIClient


# Указываем с помощью декоратора, что тест будет работать с бд.
@pytest.mark.django_db
def test_api():
    # Arrange
    # Опишем клиента, который будет отправлять запросы на наш api.
    client = APIClient()

    # Act
    # Отправим get-запрос на нужный маршрут.
    response = client.get('/messages/')

    # Assert
    # Проверим успешный статус ответа.
    assert response.status_code == 200
