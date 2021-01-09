from rest_framework import serializers
from .models import *


class AmbassadorSerializer(serializers.Serializer):
    class Meta:
        model = AmbassadorDetail
        fields = '__all__'