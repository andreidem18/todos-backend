# Generated by Django 2.2.24 on 2022-01-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20220107_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='priority',
        ),
    ]
