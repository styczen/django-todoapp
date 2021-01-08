from django.db import models
from datetime import date


class Task(models.Model):
    content = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(default=date.today)
    created_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

