# Generated by Django 4.2.7 on 2023-11-11 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='freeTimeId',
            new_name='activityId',
        ),
    ]
