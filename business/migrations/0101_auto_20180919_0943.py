# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 09:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0100_auto_20180919_0930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DayTradeDetail',
            new_name='ShopDayTrade',
        ),
        migrations.RemoveField(
            model_name='chair',
            name='time_slots',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='chairs',
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 26, 9, 43, 5, 583998), null=True),
        ),
    ]
