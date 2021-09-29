from django.urls import path
from .apiViews import CreateTaskAPIView, UpdateTaskAPIView, TaskListAPIView

app_name = 'task'
urlpatterns = [
    path('create', CreateTaskAPIView.as_view(), name='create-task'),
    path('list',TaskListAPIView.as_view(), name='display-task-list'),
    path('task-list',CreateTaskAPIView.as_view(), name='display-task-list'),
    path('<int:pk>/display',UpdateTaskAPIView.as_view(), name='display-task-detail'),
    path('delete/<int:pk>',UpdateTaskAPIView.as_view(), name='delete-task')
]
