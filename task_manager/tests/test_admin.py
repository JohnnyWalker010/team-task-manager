from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Position, Worker, TaskType, Task


class AdminSiteTest(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="test_username",
            email="test@email.com",
            password="test_password",
        )
        self.client.force_login(self.admin_user)
        self.worker = Worker.objects.create_user(
            username="test_worker",
            password="test_worker_password",
            position=Position.objects.create(name="test_position"),
        )
        self.task = Task.objects.create(
            name="test_task",
            deadline=date(2050, 1, 1),
            task_type=TaskType.objects.create(name="test_task_type"),
        )

    def test_worker_position_displayed(self):
        url = reverse("admin:task_manager_worker_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position.name)

    def test_add_worker_position_displayed(self):
        url = reverse("admin:task_manager_worker_add")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position.name)

    def test_task_description_displayed(self):
        url = reverse("admin:task_manager_task_changelist")
        response = self.client.get(url)
        self.assertContains(response, "name")
        self.assertContains(response, "description")
