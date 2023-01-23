# Generated by Django 4.1.5 on 2023-01-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0002_delete_fooditem_delete_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('member', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='marketcost',
        ),
    ]
