# Generated by Django 3.0.6 on 2020-06-03 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0008_auto_20200603_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='vehicle_number_plate',
            new_name='vehicles_number_plates',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='vehicle_precrash_factors',
            new_name='vehicles_precrash_factors',
        ),
    ]