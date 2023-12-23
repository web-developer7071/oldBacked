# Generated by Django 3.2.6 on 2022-10-15 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otherAdmin', '0004_rename_city_otherdata_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FacilityImage', models.ImageField(blank=True, default='facility.png', upload_to='otherfacilityimg/')),
                ('FacilityName', models.CharField(max_length=100)),
                ('FacilityDesc', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('otherdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='otherAdmin.otherdata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_facilities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
