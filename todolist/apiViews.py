from rest_framework import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Task, TaskList
from .serializers import TaskListSerializer, TaskSerializer


class CreateTaskListAPIView(ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class UpdateTaskListAPIView(RetrieveDestroyAPIView):
    queryset = TaskList.objects.get(id=id)
    serializer_class = TaskListSerializer

class CreateTaskAPIView(ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer

class UpdateTaskAPIView(RetrieveDestroyAPIView):
    queryset = Task.objects.get(id=id)
    serializer_class = TaskSerializer



