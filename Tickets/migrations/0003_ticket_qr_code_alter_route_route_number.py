# Generated by Django 5.0.3 on 2024-03-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_number',
            field=models.IntegerField(),
        ),
    ]
