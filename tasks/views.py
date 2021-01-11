from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

from auth0authorization.views import requires_scope


@api_view(['GET'])
@requires_scope('read:messages')
class CreateNewTask(APIView):
    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        pass


@api_view(['GET'])
@requires_scope('read:messages')
def getAllTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@requires_scope('read:messages')
def ambassadorTaskDetail(request):
    task_id = request.data.get('task_id')
    try:
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@requires_scope('read:messages')
def managerTaskDetail(request):
    task_serial = request.data.get('task_serial')
    try:
        tasks = Task.objects.filter(serial=task_serial)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def taskCompleted(request):
    pass
