# Generated by Django 4.0.1 on 2022-01-05 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_room_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumption',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 21, 46, 59, 119159)),
        ),
    ]
