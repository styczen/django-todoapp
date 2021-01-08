from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .models import Task
from .forms import TaskForm, TaskEditForm


class ToDoView(View):
    def get(self, request):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, 'todo/todo_list.html', {'tasks': tasks, 'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:home')
        tasks = Task.objects.all()
        return render(request, 'todo/todo_list.html', {'tasks': tasks, 'form': form})


class EditTask(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskEditForm(instance=task)
        context = {'edit_task_form': form}
        return render(request, 'todo/edit_task.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # TODO: needs some handling when form is invalid
        else:
            print(dir(form))
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
            context = {'edit_task_form': form}
            return render(request, 'todo/edit_task.html', context)
        return redirect('todo:home')


class DeleteTask(View):
    def get(self, request, pk):
        return render(request, 'todo/delete_task.html')

    def post(self, request, pk):
        Task.objects.filter(pk=pk).delete()
        return redirect('todo:home')


class MyDayView(View):
    def get(self, request):
        my_day_tasks = Task.objects.filter(due_date=datetime.now())
        return render(request, 'todo/my_day_tasks.html', {'tasks': my_day_tasks})

