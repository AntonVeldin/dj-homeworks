
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
# Добавим проверку, имеет ли пользователь право на работу с ресурсом.
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
# Возвращаем true, если пользователь в запросе совпадает с владельцем из объекта
        return request.user == obj.user
