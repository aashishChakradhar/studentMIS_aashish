# Generated by Django 5.0.3 on 2024-04-05 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_app', '0010_alter_attendence_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='current_semister',
        ),
        migrations.RemoveField(
            model_name='students',
            name='current_year',
        ),
    ]
