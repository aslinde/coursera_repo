# Generated by Django 5.1.7 on 2025-04-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='shift',
            field=models.IntegerField(default=0),
        ),
    ]
