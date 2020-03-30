from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_todo/',views.add_todo, name = 'add_todo'),
    path('remove_todo/<int:todo_id>/',views.remove_todo, name = 'remove_todo'),
]
