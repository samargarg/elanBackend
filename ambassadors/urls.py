from django.urls import path
from . import views


urlpatterns = [
    path('addNewAmbassador/', views.addNewAmbassador, name="addNewAmbassador"),
    path('getAmbassadorsData/', views.getAmbassadorsData, name="getAmbassadorsData"),
    path('getAmbassadorProfile/', views.getAmbassadorProfile, name="getAmbassadorProfile"),
    path('getLeaderBoardRecords/', views.getLeaderBoardRecords, name="getLeaderBoardRecords")
]