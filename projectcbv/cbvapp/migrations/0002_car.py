# Generated by Django 5.1 on 2024-09-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=256)),
                ('license_plate', models.CharField(max_length=256)),
                ('manufacturing_year', models.PositiveIntegerField()),
            ],
        ),
    ]
