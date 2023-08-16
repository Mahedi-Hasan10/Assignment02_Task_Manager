from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task.models import TaskModel
from task.forms import TaskForm
from django.shortcuts import render,redirect

# Create your views here.

class TaskListView(ListView):
    model = TaskModel
    template_name = 'task.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('show_task')
    
class TaskUpdateView(UpdateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('show_task')

class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    success_url = reverse_lazy('show_task')
    
def Compleated_task(request):
    tasks = TaskModel.objects.all().filter(is_completed= True)
    return render(request,'completed_task.html',{'completed_tasks':tasks})
def taskDone(request,id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('show_task')
