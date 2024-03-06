from django.urls import path

from task_manager.views import (
    index,
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
)

app_name = "task_manager"

urlpatterns = [
    path("", index, name="index"),
    path("workers_list/", WorkerListView.as_view(), name="workers_list"),
    path("workers_list/create", WorkerCreateView.as_view(), name="create_worker"),
    path("workers/<int:pk>/", WorkerUpdateView.as_view(), name="update_worker"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="delete_worker"),
]
