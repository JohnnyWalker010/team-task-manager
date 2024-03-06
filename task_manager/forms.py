from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
            "email"
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["position", "email"]