from django.urls import path
from . import views


url_patterns = [
    path('getAmbassadorsData/', views.GetAmbassadorsData.as_view(), name="getAmbassadorsData"),
    path('getAmbassadorProfile/', views.GetAmbassadorProfile.as_view(), name="getAmbassadorProfile")
]