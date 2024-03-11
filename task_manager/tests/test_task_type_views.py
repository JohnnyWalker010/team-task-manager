from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import TaskType

TASK_TYPE_URL = reverse("task_manager:task_types_list")


class PublicTaskTypeTests(TestCase):
    def test_login_required(self):
        response = self.client.get(TASK_TYPE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTypeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test_username")
        self.client.force_login(self.user)

    def test_retrieve_task_types(self):
        TaskType.objects.create(
            name="Test task type",
        )
        response = self.client.get(TASK_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(list(task_types), list(response.context["task_types"]))
        self.assertTemplateUsed(response, "task_manager/task_types_list.html")
