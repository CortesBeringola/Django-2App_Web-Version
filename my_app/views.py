from django.shortcuts import render
from . import models
from django.utils import timezone
from django.http import HttpResponseRedirect

def home(request):
    todo_items = models.Todo.objects.all().order_by("-added_date")
    stuff_for_frontend = {
        'todo_items':todo_items,
    }
    return render(request,'my_app/index.html',stuff_for_frontend)

def add_todo(request):
    added_date = timezone.now()
    todo = request.POST["todo"]
    models.Todo.objects.create(added_date=added_date,todo=todo)
    return HttpResponseRedirect("/")

def remove_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
