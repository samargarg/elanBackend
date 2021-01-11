from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *
import requests
import json

from auth0authorization.views import requires_scope


@api_view(['POST'])
@permission_classes([AllowAny])
def addNewAmbassador(request):
    access_token = request.data.get('access_token')
    auth0_domain = 'phantom168.us.auth0.com'
    url = f'https://{auth0_domain}/userinfo'
    body = {

    }
    headers = {
        "Authorization": f'Bearer {access_token}'
    }

    x = requests.post(url=url, json=body, headers=headers)
    data = x.json()
    print(data)
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@requires_scope('read:messages')
def getAmbassadorsData(request):
    ambassador_details = AmbassadorDetail.objects.all()
    serializer = AmbassadorDetailSerializer(ambassador_details, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@requires_scope('read:messages')
def getAmbassadorProfile(request):
    ambassador_id = request.data.get('ambassador_id')
    try:
        ambassador = User.objects.get(pk=ambassador_id)
        ambassador_detail = ambassador.ambassador_detail
        serializer = AmbassadorDetailSerializer(ambassador_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@requires_scope('read:messages')
def getLeaderBoardRecords(request):
    ambassador_details = AmbassadorDetail.objects.order_by('score')
    serializer = AmbassadorDetailSerializer(ambassador_details, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
