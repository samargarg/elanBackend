from rest_framework import serializers
from . import models


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Applicant
        fields = '__all__'