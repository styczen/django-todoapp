# Generated by Django 3.1.4 on 2021-01-07 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210107_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]