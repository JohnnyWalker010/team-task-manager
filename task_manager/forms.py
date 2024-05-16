from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker, Task, Position, TaskType


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class WorkerCreateForm(UserCreationForm):
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        required=True,
        label="Position",
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
            "email",
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        ]


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees_list",
        ]
        widgets = {
            "deadline": forms.widgets.DateTimeInput(
                attrs={
                    "type": "date",
                    "min": str(date.today()),
                    "value": str(date.today()),
                }
            )
        }


class TaskUpdateForm(forms.ModelForm):
    assignees_list = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        required=False,
        widget=forms.SelectMultiple(),
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "priority",
            "is_completed",
            "task_type",
            "assignees_list",
        ]

        widgets = {
            "deadline": forms.widgets.DateTimeInput(
                attrs={
                    "type": "date",
                    "min": str(date.today()),
                    "value": str(date.today()),
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)
        self.fields["assignees_list"].initial = self.instance.assignees_list.all()


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search position by name"}),
    )


class PositionCreateForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = [
            "name",
        ]


class PositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = [
            "name",
        ]


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search task type by name"}),
    )


class TaskTypeCreateForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = [
            "name",
        ]


class TaskTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = [
            "name",
        ]
