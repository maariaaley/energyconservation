# Generated by Django 4.0.1 on 2022-01-05 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0013_alter_room_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 6, 14, 8, 984233, tzinfo=utc)),
        ),
    ]