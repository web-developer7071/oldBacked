# Generated by Django 3.2.6 on 2022-10-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherAdmin', '0002_auto_20220321_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherdata',
            name='Collected_No_Need',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='otherdata',
            name='Running_No_Need',
            field=models.BooleanField(default=False),
        ),
    ]
