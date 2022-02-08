from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse

def tool_list(request):
    tools = Tool.objects.all().values('name', 'notes') # only grab some attributes from our database, else we can't serialize it.
    tools_list = list(tools) # convert our artists to a list instead of QuerySet
    return JsonResponse(tools_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.