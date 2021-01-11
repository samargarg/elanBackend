from rest_framework import serializers
from .models import *


class AmbassadorDetailSerializer(serializers.Serializer):
    class Meta:
        model = AmbassadorDetail
        fields = '__all__'