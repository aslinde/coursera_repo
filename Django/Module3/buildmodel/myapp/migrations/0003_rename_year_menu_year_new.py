# Generated by Django 5.1.7 on 2025-04-05 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_cuisine_menu_course_rename_price_menu_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='year',
            new_name='year_new',
        ),
    ]
