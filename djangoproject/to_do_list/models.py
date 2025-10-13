from django.utils import timezone
from django.db import models

# Create your models here.


class Task(models.Model):
    task_id = models.AutoField(primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    

class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True, null=False)
    username = models.CharField(max_length=150, unique=False, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username