from rest_framework import viewsets

from .serializers import MedSerializer
from .serializers import UserSerializer
from meds.models import Med
from meds.models import User


class MedViewSet(viewsets.ModelViewSet):
    queryset = Med.objects.all()
    serializer_class = MedSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer