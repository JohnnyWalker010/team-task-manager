from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Worker

WORKER_URL = reverse("task_manager:workers_list")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        response = self.client.get(WORKER_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="test_worker_username",
        )
        self.user.set_password("test_worker_password")
        self.user.save()
        self.client.force_login(self.user)

    def test_retrieve_all_workers(self):
        response = self.client.get(WORKER_URL)
        self.assertEqual(response.status_code, 200)
        workers = Worker.objects.all()
        self.assertEqual(list(workers), list(response.context["workers"]))
        self.assertTemplateUsed(response, "task_manager/worker_list.html")
