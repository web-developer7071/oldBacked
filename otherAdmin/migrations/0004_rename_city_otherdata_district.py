# Generated by Django 3.2.6 on 2022-10-14 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otherAdmin', '0003_auto_20221012_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otherdata',
            old_name='City',
            new_name='District',
        ),
    ]
