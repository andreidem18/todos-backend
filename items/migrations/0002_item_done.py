# Generated by Django 2.2.24 on 2021-12-27 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
