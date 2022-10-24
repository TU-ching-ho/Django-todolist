from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.viewtodo, name='viewtodo'),
    path('create/', views.create_todo, name='createtodo'),
]
