# from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Truck, Tool, Job
# from .forms import TruckForm, ToolForm, JobForm
from .serializers import TruckSerializer, ToolSerializer, JobSerializer

# Create your views here.
# views.py
from django.http import JsonResponse


class TruckList(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class TruckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class ToolList(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer







# def tool_list(request):
#     tools = Tool.objects.all().values('name', 'notes') 
#     tools_list = list(tools) 
#     return JsonResponse(tools_list, safe=False) 

# def truck_list(request):
#     trucks = Truck.objects.all().values('number', 'drivers', 'notes') 
#     trucks_list = list(trucks) 
#     return JsonResponse(trucks_list, safe=False)

# def job_list(request):
#     jobs = Job.objects.all().values('suggested_tools', 'address', 'scheduled', 'comments') 
#     jobs_list = list(jobs) 
#     return JsonResponse(jobs_list, safe=False)

# def job_detail
# def truck_detail