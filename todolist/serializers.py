from rest_framework import serializers 
from .models import Task

class TaskListSerializer(serializers.Serializer):
        tasks = serializers.CharField(max_length=255)
        fields = ['tasks']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task', 'due_date', 'task_list', 'id')

