from django.urls import path 
from task.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,Compleated_task,taskDone

urlpatterns = [
    path('',TaskListView.as_view(),name='show_task'),
    path('create/',TaskCreateView.as_view(),name ='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('completed_task/', Compleated_task, name='task_complete'),
    path('taskdone/<int:id>',taskDone,name='task_done'),
]
