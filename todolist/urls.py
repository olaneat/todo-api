from django.urls import path
from .apiViews import CreateTaskAPIView, UpdateTaskAPIView

app_name = 'task'
urlpatterns = [
    path('create', CreateTaskAPIView.as_view(), name='create-task'),
    path('dislpay',CreateTaskAPIView.as_view(), name='display-task-list'),
    path('dislpay/<int:pk>',UpdateTaskAPIView.as_view(), name='display-task-detail'),
    path('delete/<int:pk>',UpdateTaskAPIView.as_view(), name='delete-task')
]