# Generated by Django 5.0.7 on 2024-07-21 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('year_founded', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('size_range', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('linkedin_url', models.CharField(max_length=255)),
                ('current_employee_estimate', models.CharField(max_length=255)),
                ('total_employee_estimate', models.CharField(max_length=255)),
                ('uploaded_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csv_data', to='querybuilder.uploadedfile')),
            ],
        ),
    ]
