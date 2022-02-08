from django import forms
from .models import Truck,Tool,Job

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ('number', 'drivers', 'notes')


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('name', 'notes')


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('suggested_tools', 'address', 'scheduled', 'comments')
