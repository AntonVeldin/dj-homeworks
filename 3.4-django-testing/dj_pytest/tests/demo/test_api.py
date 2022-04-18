import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from demo.models import Message


# Добавим фикстуру, которая будет возвращать клиент.
@pytest.fixture
def client():
    return APIClient()


# Добавим фикстуру, которая будет создавать пользователя.
@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.mark.django_db
def test_get_messages(client, user):
    # Arrange
    # client = APIClient()
    # Создадим пользователя.
    # User.objects.create_user('admin')
    # Создадим тестовое сообщение от созданного пользователя.
    Message.objects.create(user_id=user.id, text='test_msg')

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


@pytest.mark.django_db
def test_create_message(client, user):
    # Запросим из бд количество сообщений.
    count = Message.objects.count()

# Создадим сообщение. Укажем формат передачи данных и в словаре data передадим нужные параметры.
#     response = client.post('/messages/', data={'user': user.id, 'text': 'test text'}, format='json')
# Добавим в настройки формат по умолчанию - json.
    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'}, format='json')

# Проверим сохранение объекта.
    assert response.status_code == 201
# Проверим, увеличилось ли количество сообщений после размещения нового.
    assert Message.objects.count() == count + 1
