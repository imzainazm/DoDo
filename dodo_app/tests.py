from django.test import TestCase
from django.urls import reverse
from .models import Task, Project
from django.contrib.auth.models import User
from django.utils import timezone

class TaskListViewTests(TestCase):
    def test_task_list_view(self):
        user = User.objects.create_user(username='fooUser', password='ilovemesomesecurepassword')
        project = Project.objects.create(name='Half-life', description='Dummy description')
        task = Task.objects.create(title='Make gravity gun stronger', description='Dummy description', project=project, completed=False, deadline=timezone.now() + timezone.timedelta(days=9))
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 404) #intentional failure
        self.assertContains(response, 'Make gravity gun stronger')

    def test_task_detail_view(self):
        user = User.objects.create_user(username='fooUser', password='ilovemesomesecurepassword')
        project = Project.objects.create(name='Half-life', description='Dummy description')
        task = Task.objects.create(title='Make gravity gun stronger', description='Dummy description', project=project, completed=False, deadline=timezone.now() + timezone.timedelta(days=12))
        url = reverse('task_detail', args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Make gravity gun stronger')
        self.assertContains(response, 'Dummy description')

class ProjectModelTests(TestCase):
    def test_project_str(self):
        project = Project.objects.create(name='Half-life', description='Dummy description')
        self.assertEqual(str(project), 'Half-life')

class ProjectCreateViewTests(TestCase):
    def test_project_create_view(self):
        user = User.objects.create_user(username='fooUser', password='ilovemesomesecurepassword')
        self.client.force_login(user)
        response = self.client.post(reverse('create_project'), {'name': 'Half-life', 'description': 'Dummy description'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(name='Half-life').exists())

class TaskCreateViewTests(TestCase):
    def test_task_create_view(self):
        user = User.objects.create_user(username='fooUser', password='ilovemesomesecurepassword')
        project = Project.objects.create(name='Half-life', description='Dummy description')
        self.client.force_login(user)
        response = self.client.post(reverse('create_task'), {'title': 'Make gravity gun stronger', 'description': 'Dummy description', 'project': project.id, 'deadline': timezone.now() + timezone.timedelta(days=9), 'completed': False})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='Make gravity gun stronger').exists())
