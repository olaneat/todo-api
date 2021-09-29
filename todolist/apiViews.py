from rest_framework.generics import  ListCreateAPIView, ListAPIView,  RetrieveDestroyAPIView
from .models import Task, TaskList
from .serializers import TaskSerializer


class CreateTaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTaskAPIView(ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer

class UpdateTaskAPIView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



