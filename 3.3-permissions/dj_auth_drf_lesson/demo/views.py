from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from demo.models import Adv
from demo.permission import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from demo.serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
# Добавим кастомный класс с ограничением IsOwnerOrReadOnly.
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
# Добавим троттлинг для анонимных пользователей.
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
