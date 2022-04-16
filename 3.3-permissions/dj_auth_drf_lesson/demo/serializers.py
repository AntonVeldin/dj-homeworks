from rest_framework import serializers

from demo.models import Adv


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'open']
# Указываем поля, которые не надо передавать в теле.
# Это поля, которые будут доступны только для чтения.
        read_only_fields = ['user',]
