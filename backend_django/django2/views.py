from django.shortcuts import render, redirect
from .models import Truck, Tool, Job
# Create your views here.
# views.py
from django.http import JsonResponse

def tool_list(request):
    tools = Tool.objects.all().values('name', 'notes') # only grab some attributes from our database, else we can't serialize it.
    tools_list = list(tools) # convert our artists to a list instead of QuerySet
    return JsonResponse(tools_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

def truck_list(request):
    trucks = Truck.objects.all().values('number', 'drivers', 'notes') 
    trucks_list = list(trucks) 
    return JsonResponse(trucks_list, safe=False)

def job_list(request):
    jobs = Job.objects.all().values('suggested_tools', 'address', 'scheduled', 'comments') 
    jobs_list = list(jobs) 
    return JsonResponse(jobs_list, safe=False)

def job_detail
def truck_detail