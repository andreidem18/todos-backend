# Generated by Django 2.2.24 on 2022-01-07 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='done',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item',
        ),
        migrations.RemoveField(
            model_name='item',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='item',
            name='todo',
        ),
    ]
