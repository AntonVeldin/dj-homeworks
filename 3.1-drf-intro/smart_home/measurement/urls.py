from django.urls import path

from measurement.views import (
    SensorListView,
    SensorRetrieveUpdateView,
    MeasurementCreateView
)

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
