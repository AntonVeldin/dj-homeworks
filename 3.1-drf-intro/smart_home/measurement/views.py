from measurement.models import Sensor, Measurement
from rest_framework.generics import (
    RetrieveUpdateAPIView,
    CreateAPIView,
    ListCreateAPIView
)
from measurement.serializers import (
    SensorSerializer,
    SensorMeasurementSerializer,
    MeasurementCreateSerializer
)


class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorMeasurementSerializer
