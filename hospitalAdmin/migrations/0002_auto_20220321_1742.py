# Generated by Django 3.2.6 on 2022-03-21 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAdmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collected_live_prescription',
            name='user',
        ),
        migrations.RemoveField(
            model_name='current_live_status',
            name='user',
        ),
        migrations.RemoveField(
            model_name='running_live_prescription',
            name='user',
        ),
        migrations.RemoveField(
            model_name='today_live_status',
            name='user',
        ),
    ]
