from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_task_list'),
    path('api/tasks/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='api_task_detail'),
    path('api/projects/', views.ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_project_list'),
    path('api/projects/<int:pk>/', views.ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='api_project_detail'),
    path('', views.task_list, name='task_list'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.create_project, name='create_project'),
    path('tasks/create/', views.create_task, name='create_task'),
]