from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit-task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
    
]
