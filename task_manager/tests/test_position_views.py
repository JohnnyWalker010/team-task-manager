from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Position

POSITION_URL = reverse("task_manager:positions_list")


class PublicPositionTests(TestCase):
    def test_login_required(self):
        response = self.client.get(POSITION_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivatePositionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test_username")
        self.client.force_login(self.user)

    def test_retrieve_positions(self):
        Position.objects.create(
            name="Test Position",
        )
        response = self.client.get(POSITION_URL)
        self.assertEqual(response.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(list(positions), list(response.context["positions"]))
        self.assertTemplateUsed(response, "task_manager/position_list.html")
