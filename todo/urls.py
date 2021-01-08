from django.urls import path
from todo.views import ToDoView, EditTask, DeleteTask, MyDayView

app_name = 'todo'

urlpatterns = [
    path('', ToDoView.as_view(), name='home'),
    path('edit/<int:pk>', EditTask.as_view(), name='edit_task'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('my-day-tasks', MyDayView.as_view(), name='my_day_tasks'),
]

