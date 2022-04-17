from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from demo.models import Adv
from rest_framework.permissions import IsAuthenticated
from demo.serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
# Опишем разделение прав.
# Передаем список с требуемыми разрешениями для манипуляций.
    permission_classes = [IsAuthenticated, ]
    # throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
