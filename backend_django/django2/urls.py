from django.urls import path
from . import views
# below for auth
# from rest_framework.routers import defaultRouter

urlpatterns = [
    path('tools/', views.ToolList.as_view(), name='tool_list'),
    path('tools/<int:pk>', views.ToolDetail.as_view(), name='tool_detail'),
    path('trucks/', views.TruckList.as_view(), name="truck_list"),
    path('trucks/<int:pk>', views.TruckDetail.as_view(), name="truck_detail"),
    path('jobs/', views.JobList.as_view(), name="song_list"),
    path('jobs/<int:pk>', views.JobDetail.as_view(), name="song_detail"),

]
