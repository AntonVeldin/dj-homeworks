# from rest_framework.response import Response
# from rest_framework.viewsets import ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    # Указываем QuerySet из которого будем брать все наши данные
    queryset = Comment.objects.all()
    # Указываем сериализатор с помощью которого все объекты будут превращаться
    # в json и обратно. Его опишем в serializers.py.
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user',]
    search_fields = ['text',]
    ordering_fields = ['id', 'user', 'text', 'created_at']
    pagination_class = LimitOffsetPagination


# class CommentViewSet1(ViewSet):
#
#     # Выводит все объекты данного ресурса
#     def list(self, request):
#         return Response({'status': 'ok'})
#
#     # Смотреть конкретный объект
#     def retrieve(self, request):
#         pass
#
#     # Для удаления объекта
#     def destoy(self, request):
#         pass
#
#     # Для обновления объекта
#     def update(self, request):
#         pass
#
#     # Для создания объекта
#     def create(self, request):
#         pass

