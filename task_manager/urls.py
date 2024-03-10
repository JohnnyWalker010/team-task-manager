from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from task_manager.views import (
    index,
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)

app_name = "task_manager"

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("workers_list/", WorkerListView.as_view(), name="workers_list"),
    path("workers_list/create", WorkerCreateView.as_view(), name="create_worker"),
    path("workers/<int:pk>/", WorkerUpdateView.as_view(), name="update_worker"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="delete_worker"),
    path("tasks_list/", TaskListView.as_view(), name="tasks_list"),
    path("tasks_list/create", TaskCreateView.as_view(), name="create_task"),
    path("tasks_list/<int:pk>", TaskUpdateView.as_view(), name="update_task"),
    path("tasks_list/<int:pk>/delete", TaskDeleteView.as_view(), name="delete_task"),
    path("positions_list/", PositionListView.as_view(), name="positions_list"),
    path("positions_list/create", PositionCreateView.as_view(), name="create_position"),
    path(
        "positions_list/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="update_position",
    ),
    path(
        "positions_list/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="delete_position",
    ),
    path("task_types_list/", TaskTypeListView.as_view(), name="task_types_list"),
    path(
        "task_types_list/create", TaskTypeCreateView.as_view(), name="create_task_type"
    ),
    path(
        "task_types_list/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="update_task_type",
    ),
    path(
        "task_types_list/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="delete_task_type",
    ),
]
