# Generated by Django 3.2.6 on 2022-10-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAdmin', '0005_rename_city_hospitaldata_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetail',
            name='Collected_No_Need',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='Running_No_Need',
            field=models.BooleanField(default=False),
        ),
    ]
