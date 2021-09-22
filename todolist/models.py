from django.db import models
from django.db.models.base import Model
from .constants import task_list
# Create your models here.

class TaskList(models.Model):
    task_list = models.CharField(max_length=250, choices=task_list)

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'
    
    def __str__(self):
        return self.task_list

class Task(models.Model):
    task = models.TextField()
    due_date = models.DateField(auto_now=True)
    due_time = models.DateTimeField(default=True)
    task_lists = models.ForeignKey(TaskList, blank=True, null=True, on_delete=models.CASCADE, related_name='task_lists') 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return self.task
    
