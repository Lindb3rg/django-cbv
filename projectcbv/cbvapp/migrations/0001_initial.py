# Generated by Django 5.1 on 2024-09-18 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('principal', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='cbvapp.school')),
            ],
        ),
    ]
