# Generated by Django 3.0.6 on 2020-06-09 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0012_auto_20200609_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='nearest_landmark',
        ),
        migrations.AddField(
            model_name='incident',
            name='address_or_nearest_landmark',
            field=models.CharField(default=0, help_text='By landmark we mean somewhere notable such as bustop, market, hotel, hospital etc.', max_length=50, verbose_name='address and/or nearest landmark'),
            preserve_default=False,
        ),
    ]