# Generated by Django 4.1.5 on 2023-01-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_one', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='slug',
        ),
    ]
