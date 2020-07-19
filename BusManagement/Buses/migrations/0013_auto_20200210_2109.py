# Generated by Django 2.2.1 on 2020-02-10 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buses', '0012_auto_20200119_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_description',
            name='dates',
            field=models.DateField(default=datetime.date(2020, 2, 10)),
        ),
        migrations.AlterField(
            model_name='bus_description',
            name='pick_time',
            field=models.TimeField(default=datetime.time(21, 9, 33, 206336)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 10, 21, 9, 33, 206336)),
        ),
    ]
