# Generated by Django 4.1.5 on 2023-01-26 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0011_remove_meal_name_meal_date_meal_person_1_meal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='parson_1',
        ),
    ]
