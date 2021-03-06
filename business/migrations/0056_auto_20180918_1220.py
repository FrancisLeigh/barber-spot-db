# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 12:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0055_auto_20180918_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='openclosetimes',
            name='trading_time_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TradingTime'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 12, 20, 56, 836726), null=True),
        ),
    ]
