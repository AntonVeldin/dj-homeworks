# TODO: опишите необходимые обработчики, рекомендуется
#  использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
