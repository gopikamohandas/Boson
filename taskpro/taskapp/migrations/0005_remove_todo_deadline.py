# Generated by Django 5.1.4 on 2024-12-06 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_alter_todo_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Deadline',
        ),
    ]