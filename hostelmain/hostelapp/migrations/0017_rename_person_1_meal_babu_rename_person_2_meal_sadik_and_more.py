# Generated by Django 4.1.5 on 2023-01-31 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0016_remove_meal_person_1_meal_meal_person_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='person_1',
            new_name='Babu',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='person_2',
            new_name='Sadik',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='person_3',
            new_name='Shakil',
        ),
    ]