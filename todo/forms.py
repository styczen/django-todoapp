from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'due_date']


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

