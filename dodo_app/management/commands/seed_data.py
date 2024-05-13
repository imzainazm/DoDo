from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dodo_app.models import Project, Task

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):

        user1 = User.objects.create_user(username='user1', email='user1@example.com', password='password')
        user2 = User.objects.create_user(username='user2', email='user2@example.com', password='password')

        project1 = Project.objects.create(name='BugKong', description='BugZilla but team Kong')
        project2 = Project.objects.create(name='Glizzle', description='Slack but with a G')

        Task.objects.create(title='Bug resolution', description='Story to track bug resolution', project=project1, completed=False, deadline='2024-06-06')
        Task.objects.create(title='Make the logo bigger', description='Task to increase logo size by 1 pixel', project=project1, completed=False, deadline='2024-06-06')
        Task.objects.create(title='Change the background color to #FFFFE4', description='Change the color to #FFFFE4', project=project2, completed=False, deadline='2024-06-06')
        Task.objects.create(title='Add Gen AI to todo app', description='TODO app should already know what the user wants to type.', project=project2, completed=False, deadline='2024-06-06')

        self.stdout.write(self.style.SUCCESS('Seed data created successfully.'))