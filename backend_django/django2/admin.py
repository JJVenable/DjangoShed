from django.contrib import admin
from .models import Truck
from .models import Tool
from .models import Job
# Register your models here.

admin.site.register(Truck)
admin.site.register(Tool)
admin.site.register(Job)
