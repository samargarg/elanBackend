from django.urls import path
from . import views


urlpatterns = [
    path('getAmbassadorsData/', views.GetAmbassadorsData.as_view(), name="getAmbassadorsData"),
    path('getAmbassadorProfile/', views.GetAmbassadorProfile.as_view(), name="getAmbassadorProfile")
]