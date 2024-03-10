from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Task, TaskType

TASK_URL = reverse("task_manager:tasks_list")


class PublicTaskTests(TestCase):
    def test_login_required(self):
        response = self.client.get(TASK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test_username")
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        Task.objects.create(
            name="Test Task",
            deadline="2050-01-10",
            task_type=TaskType.objects.create(name="Task Type"),
        )
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(tasks), list(response.context["tasks"]))
        self.assertTemplateUsed(response, "task_manager/task_list.html")
