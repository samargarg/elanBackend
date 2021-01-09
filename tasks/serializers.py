from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = '__all__'