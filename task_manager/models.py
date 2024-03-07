from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
    )
    groups = models.ManyToManyField(Group, related_name="workers")
    user_permissions = models.ManyToManyField(
        Permission, related_name="workers_permissions"
    )

    def __str__(self):
        return f"{self.username} - ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Ordinary", "Ordinary"),
        ("Low", "Low"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10, default="Ordinary", choices=PRIORITY_CHOICES
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees_list = models.ManyToManyField(Worker)

    def __str__(self):
        return f"{self.task_type} - {self.name} (Priority: {self.priority})"
