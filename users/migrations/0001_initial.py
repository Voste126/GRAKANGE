# Generated by Django 5.0.4 on 2024-04-29 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FName', models.CharField(max_length=100)),
                ('SurName', models.CharField(max_length=100)),
                ('NationalID', models.BigIntegerField(blank=True)),
                ('Phone', models.BigIntegerField(blank=True)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('County', models.CharField(blank=True, max_length=100)),
                ('SubCounty', models.CharField(blank=True, max_length=100)),
                ('Ward', models.CharField(blank=True, max_length=100)),
                ('Location', models.CharField(blank=True, max_length=100)),
                ('SubLocation', models.CharField(blank=True, max_length=100)),
                ('LandSize', models.FloatField(blank=True)),
                ('Speciality', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FarmName', models.CharField(max_length=100)),
                ('FarmSize', models.FloatField()),
                ('FarmLocation', models.CharField(max_length=100)),
                ('FarmSpeciality', models.CharField(max_length=100)),
                ('Farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.farmer')),
            ],
        ),
    ]
