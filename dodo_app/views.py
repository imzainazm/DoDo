from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Task, Project
from .serializers import TaskSerializer, ProjectSerializer
from .forms import TaskForm, ProjectForm

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def task_list(request):
    projects = Project.objects.prefetch_related('tasks').all()
    return render(request, 'task_list.html', {'projects': projects})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})