from rest_framework import serialilzers 
from .models import Task, TaskList

class TaskLIstSerializer(serialilzers.Serializer):
    class Meta:
        model = TaskList
        fields = '__all__'


class TaskSerializer(serializers.Serializer):
    task_list = TaskLIstSerializer()
    class Meta:
        model = Task
        fields = ('task', 'due_date', 'task_list',)

        