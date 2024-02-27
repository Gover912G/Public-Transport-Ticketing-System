# Generated by Django 5.0.2 on 2024-02-21 13:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.UUIDField(default=uuid.uuid4)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('accepted_date', models.DateTimeField(blank=True, null=True)),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('ticket_status', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_number', models.IntegerField(max_length=5)),
                ('route_name', models.CharField(max_length=100)),
                ('stage', models.ManyToManyField(to='Tickets.stage')),
            ],
        ),
    ]
