from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class CreateNewTask(APIView):
    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        ass



class GetAllTasks(APIView):
    pass
