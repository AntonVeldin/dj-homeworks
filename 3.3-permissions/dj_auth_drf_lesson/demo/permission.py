
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
# Добавим исключение при get-запросе.
# Проверку на собственность будет проходить любой пользователь.
        if request.method == 'GET':
            return True
        return request.user == obj.user
