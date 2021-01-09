from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *


class AddNewAmbassador(APIView):
    def post(self, request):



class GetAmbassadorsData(APIView):
    def get(self, request):
        ambassadors = User.objects.filter(is_staff=True)
        serializer = AmbassadorSerializer(ambassadors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAmbassadorProfile(APIView):
    def get(self, request):
        ambassador_id = request.data.get('ambassador_id')
        ambassador = User.objects.get(pk=ambassador_id)
        serializer = AmbassadorSerializer(ambassador)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetLeaderBoardRecords(APIView):
    pass