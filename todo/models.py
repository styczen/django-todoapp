from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(auto_now=False, auto_now_add=False)

