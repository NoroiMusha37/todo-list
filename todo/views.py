from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "todo/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
