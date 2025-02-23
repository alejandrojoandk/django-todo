from django.contrib.auth import get_user_model
from django.urls import reverse
from base.models import Task
from django.test import TestCase

class TestViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('login'), data)
        self.assertRedirects(response, reverse('tasks'))

    def test_task_create_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')

        data = {'title': 'New Task', 'description': 'Task description', 'complete': False}
        response = self.client.post(reverse('task-create'), data)

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'New Task')

        self.assertRedirects(response, reverse('tasks'))

    def test_task_update_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')

        task = Task.objects.create(title="Old Task", user=self.user, complete=False)

        data = {'title': 'Updated Task', 'description': 'Updated description', 'complete': True}
        response = self.client.post(reverse('task-update', args=[task.id]), data)

        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task')
        self.assertTrue(task.complete)

        self.assertRedirects(response, reverse('tasks'))

    def test_task_delete_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')

        task = Task.objects.create(title="Task to delete", user=self.user, complete=False)

        response = self.client.post(reverse('task-delete', args=[task.id]))

        self.assertEqual(Task.objects.count(), 0)

        self.assertRedirects(response, reverse('tasks'))

    def test_task_list_view_not_authenticated(self):
        response = self.client.get(reverse('tasks'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('tasks')}")