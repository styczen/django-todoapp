from django.test import TestCase
from todo.models import Task
from datetime import date, timedelta


class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(content='First test content', due_date=date(2020, 1, 1))

    def test_task_content(self):
        task_content = Task.objects.get(id=1).content
        self.assertEqual(task_content, 'First test content')

    def test_task_due_date(self):
        task_due_date = Task.objects.get(id=1).due_date
        self.assertEqual(task_due_date, date(2020, 1, 1))

    def test_task_created_date(self):
        task_created_date = Task.objects.get(id=1).created_date_time
        year = task_created_date.year
        month = task_created_date.month
        day = task_created_date.day
        today = date.today()
        self.assertEqual(year, today.year) 
        self.assertEqual(month, today.month) 
        self.assertEqual(day, today.day) 

    def test_str_method(self):
        task_str = str(Task.objects.get(id=1))
        self.assertEqual(task_str, 'First test content')

