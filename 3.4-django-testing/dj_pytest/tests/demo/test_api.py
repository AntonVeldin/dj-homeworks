import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from demo.models import Message


@pytest.mark.django_db
def test_api():
    # Arrange
    client = APIClient()
    # Создадим пользователя.
    User.objects.create_user('admin')
    # Создадим тестовое сообщение от созданного пользователя.
    Message.objects.create(user_id=1, text='test_msg')

    # Act
    response = client.get('/messages/')

    # Assert
    assert response.status_code == 200
    # Обратимся к содержимому ответа запроса.
    data = response.json()
    # Проверим наличие первого тестового сообщения.
    assert len(data) == 1
    # Проверим текст ответа созданного сообщения. В ответе словарь.
    assert data[0]['text'] == 'test_msg'

