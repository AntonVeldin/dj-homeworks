from rest_framework import serializers

from demo.models import Adv


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
# Указываем, что будет основываться на модели объявлений Adv
        model = Adv
# Укажем поля, которые необходимо отображать в виде json
        fields = ['id', 'user', 'text', 'created_at', 'open']
        # read_only_fields = ['user',]
