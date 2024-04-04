# Generated by Django 5.0.3 on 2024-04-03 07:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('roll', models.CharField(max_length=6)),
                ('fname', models.CharField(max_length=35)),
                ('lname', models.CharField(max_length=35)),
                ('year', models.CharField(max_length=1)),
                ('semister', models.CharField(max_length=10)),
                ('faculty', models.CharField(max_length=25)),
                ('programe', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=60)),
                ('guardian', models.CharField(max_length=35)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('present_days', models.IntegerField()),
                ('absent_days', models.IntegerField()),
                ('is_present', models.BooleanField(default=False)),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='attendence_app.students')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
