from django.shortcuts import render
from django.views import generic
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "todo/index.html"
