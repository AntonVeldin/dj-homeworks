from rest_framework.generics import RetrieveAPIView

from .models import Weapon
from .serializers import WeaponSerializer


class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
