from django.urls import path
from todo.views import ToDoView, EditTask, DeleteTask

app_name = 'todo'

urlpatterns = [
    path('', ToDoView.as_view(), name='home'),
    path('edit/<int:pk>', EditTask.as_view(), name='edit_task'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete_task'),
]

