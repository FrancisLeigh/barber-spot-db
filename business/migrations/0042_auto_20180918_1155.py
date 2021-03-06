# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 11:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0041_auto_20180918_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='openclosetimes',
            name='trading_times_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.TradingTimes'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 11, 55, 40, 807048), null=True),
        ),
    ]
