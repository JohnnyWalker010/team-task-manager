from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from task_manager.forms import (
    WorkerSearchForm,
    WorkerCreateForm,
    WorkerUpdateForm,
    TaskSearchForm,
    TaskCreateForm,
    TaskUpdateForm,
    PositionSearchForm,
    PositionCreateForm,
    PositionUpdateForm,
    TaskTypeSearchForm,
    TaskTypeCreateForm,
    TaskTypeUpdateForm,
)
from task_manager.models import Worker, Task, TaskType, Position, UserVisit


@login_required
def index(request):
    """View function for the home page of the site."""
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_task_types = TaskType.objects.count()
    num_positions = Position.objects.count()

    user_visit, created = UserVisit.objects.get_or_create(user=request.user)

    user_visit.num_visits += 1
    user_visit.save()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_task_types": num_task_types,
        "num_positions": num_positions,
        "num_visits": user_visit.num_visits
    }

    return render(request, "task_manager/index.html", context=context)


class WorkerListView(LoginRequiredMixin, ListView):
    model = get_user_model()
    paginate_by = 5
    context_object_name = "workers"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(initial={"username": username})

        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])

        return queryset.order_by("username")


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("task_manager:workers_list")
    template_name = "task_manager/worker_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task_manager:workers_list")
    template_name = "task_manager/worker_update_form.html"


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:workers_list")
    template_name = "task_manager/worker_delete_form.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_manager/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        queryset = Task.objects.all().order_by("name")
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_manager:tasks_list")
    template_name = "task_manager/task_create_form.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_manager/task_update_form.html"
    success_url = reverse_lazy("task_manager:tasks_list")
    form_class = TaskUpdateForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.assignees_list.set(form.cleaned_data["assignees_list"])

        return response


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_manager/task_delete_form.html"
    success_url = reverse_lazy("task_manager:tasks_list")


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "task_manager/position_list.html"
    context_object_name = "positions"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = PositionSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        queryset = Position.objects.all().order_by("name")
        form = PositionSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    template_name = "task_manager/position_create.html"
    form_class = PositionCreateForm
    success_url = reverse_lazy("task_manager:positions_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    form_class = PositionUpdateForm
    success_url = reverse_lazy("task_manager:positions_list")
    template_name = "task_manager/position_update_form.html"


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:positions_list")
    template_name = "task_manager/position_delete_form.html"


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task_manager/task_types_list.html"
    context_object_name = "task_types"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = TaskTypeSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        queryset = TaskType.objects.all().order_by("name")
        form = TaskTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    template_name = "task_manager/task_type_create.html"
    form_class = TaskTypeCreateForm
    success_url = reverse_lazy("task_manager:task_type_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    form_class = TaskTypeUpdateForm
    success_url = reverse_lazy("task_manager:task_types_list")
    template_name = "task_manager/task_type_update_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:task_types_list")
    template_name = "task_manager/task_type_delete_form.html"
