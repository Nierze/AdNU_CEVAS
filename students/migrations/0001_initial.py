# Generated by Django 5.0.3 on 2024-04-21 06:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=11)),
                ('course', models.CharField(max_length=50)),
                ('year_level', models.IntegerField()),
                ('section', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^CO\\d{4}-\\d{5}$', message='Invalid student number format')])),
            ],
        ),
    ]
