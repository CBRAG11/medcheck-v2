from rest_framework import serializers

from meds.models import Med
from meds.models import User


class MedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Med
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'