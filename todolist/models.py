from django.db import models
from .constants import task_list
import uuid 
# Create your models here.

class TaskList(models.Model):
    task_list = models.CharField(max_length=250, choices=task_list)

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'
    
    def __str__(self):
        return self.task_list

class Task(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, max_length=37, unique=True, primary_key=True)
    task = models.TextField()
    due_date = models.DateField(auto_now=True)
    task_list = models.CharField(max_length=250, choices=task_list) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return self.task
    
