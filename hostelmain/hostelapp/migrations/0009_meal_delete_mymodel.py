# Generated by Django 4.1.5 on 2023-01-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0008_mymodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parson_1', models.IntegerField(choices=[('meal_1', 'meal_1'), ('meal_2', 'meal_2'), ('meal_3', 'meal_3')])),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
