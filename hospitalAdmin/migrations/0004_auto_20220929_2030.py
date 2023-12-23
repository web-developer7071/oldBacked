# Generated by Django 3.2.6 on 2022-09-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAdmin', '0003_auto_20220928_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='Emergency_Fees',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='Operation_Time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='Other_Info',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
