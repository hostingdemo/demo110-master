# Generated by Django 3.2.4 on 2021-06-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.AddField(
            model_name='student',
            name='mobileNumber',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
