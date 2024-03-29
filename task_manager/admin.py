from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Worker, Task, Position, TaskType


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": ("first_name", "last_name", "position"),
            },
        ),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_filter = ("priority", "task_type")
    list_display = ("name", "description")


admin.site.register(TaskType)
admin.site.register(Position)
