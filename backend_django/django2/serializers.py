from rest_framework import serializers
from .models import Tool, Truck, Job  

class TruckSerializer(serializers.HyperlinkedModelSerializer):
    job = serializers.HyperlinkedRelatedField(
        view_name='job_detail',
        many=True,
        read_only=True
    )
    tool = serializers.HyperlinkedRelatedField(
        view_name='tool_detail',
        many=True,
        read_only=True
    )
    class Meta: 
      model = Truck
      fields = ('id','number', 'drivers', 'notes', 'tool', 'job')
  
class ToolSerializer(serializers.HyperlinkedModelSerializer):
    truck = serializers.HyperlinkedRelatedField(
        view_name='truck_detail',
        many=True,
        read_only=True
    )
    class Meta: 
      model = Tool
      fields = ('id','name', 'notes','truck')
  
  
class JobSerializer(serializers.HyperlinkedModelSerializer):
    truck = serializers.HyperlinkedRelatedField(
        view_name='truck_detail',
        many=True,
        read_only=True
    )
    class Meta: 
      model = Job
      fields = ('id', 'suggested_tools', 'address', 'scheduled', 'comments', 'truck')
  
