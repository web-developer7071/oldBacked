# Generated by Django 3.2.6 on 2022-10-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_term_cond'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admin_type',
        ),
        migrations.AddField(
            model_name='user',
            name='admin_service_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
