# Generated by Django 5.0.3 on 2024-04-03 09:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_app', '0004_students_attendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('subject', models.CharField(max_length=50)),
                ('subject_faculty', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='students',
            old_name='semister',
            new_name='current_semister',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='year',
            new_name='current_year',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='faculty',
            new_name='student_faculty',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='programe',
            new_name='student_programe',
        ),
        migrations.AddField(
            model_name='students',
            name='subjects',
            field=models.ManyToManyField(to='attendence_app.subjects'),
        ),
    ]
