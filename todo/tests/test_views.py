from django.test import TestCase
from todo.views import ToDoView, EditTask, DeleteTask, MyDayView
from django.test import Client
from datetime import date


class ToDoViewTests(TestCase):
    def test_get_status_code(self):
        client = Client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_post_valid_request_status_code(self):
        client = Client()
        resp = client.post('/', data={'content': 'test content', 'due_date': date.today()})
        self.assertEqual(resp.status_code, 302)

    def test_post_invalid_request_status_code(self):
        client = Client()
        resp = client.post('', data={'content': 'test content', 'due_date': 'bad date'})
        self.assertEqual(resp.status_code, 200)

