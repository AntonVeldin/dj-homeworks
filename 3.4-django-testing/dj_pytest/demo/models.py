
from django.contrib.auth.models import User
from django.db import models


# Добавим модель Сообщение
class Message(models.Model):
# Сообщение оставляет пользователь.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# У сообщения есть текст.
    text = models.TextField()
# Время создания сообщения.
    created_at = models.DateTimeField(auto_now_add=True)
