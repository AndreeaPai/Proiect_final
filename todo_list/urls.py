
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name="delete"),
    path('edit/<int:todo_id>/', views.edit, name="edit"),
]
