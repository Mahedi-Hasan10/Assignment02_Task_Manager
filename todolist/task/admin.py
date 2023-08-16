from django.contrib import admin
from task.models import TaskModel
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['taskTitle','taskDescription','is_completed']
    
admin.site.register(TaskModel,TaskModelAdmin)