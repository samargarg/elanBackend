from django.urls import path
from . import views

urlpatterns = [
    path('addNewAmbassador/', views.AddNewAmbassador.as_view(), name="addNewAmbassador"),
    path('addLocalAmbassador/', views.AddLocalAmbassador.as_view(), name="addLocalAmbassador"),
    path('getMyAmbassadorProfile/', views.GetMyAmbassadarProfile.as_view(), name="getMyAmbassadarProfile"),
    path('updateMyAmbassadorProfile/', views.UpdateMyAmbassadorProfile.as_view(), name="updateMyAmbassadarProfile"),
    path('getAmbassadorProfile/<int:ambassador_id>', views.GetAmbassadorProfile.as_view(), name="getAmbassadorProfile"),
    path('getAllAmbassadorProfiles/', views.GetAllAmbassadorProfiles.as_view(), name="getAllAmbassadorProfiles"),
    path('getLeaderBoardRecords/', views.GetLeaderBoardRecords.as_view(), name="getLeaderBoardRecords"),
    path('createNewTask/', views.CreateNewTask.as_view(), name="createNewTask"),
    path('addSelectiveTasksForUsers/', views.AddSelectiveTasksForUsers.as_view(), name="addSelectiveTasksForUsers"),
    path('getAllTasksForAmbassador/', views.GetAllTasksForAmbassador.as_view(), name="getAllTasksForAmbassador"),
    path('getAllTasksForManager/', views.GetAllTasksForManager.as_view(), name="getAllTasksForManager"),
    path('taskDetailsForAmbassador/<int:task_serial>/', views.TaskDetailsForAmbassador.as_view(), name="taskDetailsForAmbassador"),
    path('changeTaskToCompleted/<int:task_serial>/', views.ChangeTaskToCompleted.as_view(), name="changeTaskToCompleted"),
    path('awardMarksForTask/<int:task_serial>/<int:ambassador_id>/', views.AwardMarksForTask.as_view(), name="awardMarksForTask"),
    path('addComment/', views.AddComment.as_view(), name="addComment"),
    path('getAllComments/', views.GetAllComments.as_view(), name="getAllComments"),
    path('updateAmbassadorScore/', views.UpdateAmbassadorScore.as_view(), name="updateAmbassadorScore")
]