# Generated by Django 4.2.21 on 2025-06-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iptalbasvuru',
            name='mail_gonderildi',
            field=models.BooleanField(default=False),
        ),
    ]
