# Generated by Django 3.1 on 2020-11-30 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dateAdded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]