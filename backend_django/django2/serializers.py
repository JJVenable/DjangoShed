from rest_framework import serializers
from .models import Tool, Truck, Job  

class TruckSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(
        view_name='job_detail',
        many=True,
        read_only=True
    )
    tools = serializers.HyperlinkedRelatedField(
        view_name='tool_detail',
        many=True,
        read_only=True
    )
    class Meta: 
      model = Truck
      fields = ('number', 'drivers', 'notes')
  
class ToolSerializer(serializers.HyperlinkedModelSerializer):
    trucks = serializers.HyperlinkedRelatedField(
        view_name='truck_detail',
        many=True,
        read_only=True
    )
    class Meta: 
      model = Tool
      fields = ('name', 'notes')
  
  
class JobSerializer(serializers.HyperlinkedModelSerializer):
    trucks = serializers.HyperlinkedRelatedField(
        view_name='truck_detail',
        many=True,
        read_only=True
    )
    class Meta: 
      model = Job
      fields = ('suggested_tools', 'address', 'scheduled', 'comments')
  
