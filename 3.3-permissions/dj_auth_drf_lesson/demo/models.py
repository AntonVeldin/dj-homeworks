from django.contrib.auth.models import User
from django.db import models


# Опишем класс Обявление
class Adv(models.Model):
# Пользователь, кто создал объявление
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Текст объявления
    text = models.TextField()
# Дата создания
    created_at = models.DateTimeField(auto_now_add=True)
# Открыто или закрыто объявление
    open = models.BooleanField(default=True)
