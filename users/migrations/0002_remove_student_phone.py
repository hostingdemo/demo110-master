# Generated by Django 3.0.3 on 2021-06-03 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]
