from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='projects')
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
