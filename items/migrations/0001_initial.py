# Generated by Django 2.2.24 on 2021-12-27 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todos', '0001_initial'),
        ('priorities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='priorities.Priority')),
                ('todo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='todos.Todo')),
            ],
        ),
    ]
