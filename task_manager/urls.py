from django.urls import path

from task_manager.views import (
    index,
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView, TaskDeleteView,
)

app_name = "task_manager"

urlpatterns = [
    path("", index, name="index"),
    path("workers_list/", WorkerListView.as_view(), name="workers_list"),
    path("workers_list/create", WorkerCreateView.as_view(), name="create_worker"),
    path("workers/<int:pk>/", WorkerUpdateView.as_view(), name="update_worker"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="delete_worker"),
    path("tasks_list/", TaskListView.as_view(), name="tasks_list"),
    path("tasks_list/create", TaskCreateView.as_view(), name="create_task"),
    path("tasks_list/<int:pk>", TaskUpdateView.as_view(), name="update_task"),
    path("tasks_list/<int:pk>/delete", TaskDeleteView.as_view(), name="delete_task"),
]
