# Generated by Django 3.0.6 on 2020-06-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0009_auto_20200603_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='number_of_damaged_vehicles',
        ),
    ]