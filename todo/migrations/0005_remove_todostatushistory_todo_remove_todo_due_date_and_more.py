# Generated by Django 5.1 on 2024-08-16 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0004_todocomment_todostatushistory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todostatushistory",
            name="todo",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="due_date",
        ),
        migrations.DeleteModel(
            name="TodoComment",
        ),
        migrations.DeleteModel(
            name="TodoStatusHistory",
        ),
    ]
